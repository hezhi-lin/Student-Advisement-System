# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
from bs4 import BeautifulSoup
from myproject.myapp.models import *
from myproject.myapp.forms import DocumentForm
from django.http import HttpResponse
from . import extractData
from CourseGrade import *
from copy import deepcopy
import json
import subprocess
import uuid
import os

from django.contrib.auth.decorators import login_required

@login_required
def home(request):



    # newSection = UnderOrGraduateSection.objects.get(id=58)
    # courses = UnderOrGraduateCourse.objects.filter(section_id=44)
    # for course in courses:
    #     newCourse = deepcopy(course)

    #     result = UnderOrGraduateCourse.objects.filter(section_id=58,courseId=newCourse.courseId)
    #     if result.exists():
    #         print("Already exists")
    #     else :
    #         print (course.courseTitle)
    #         newCourse.section = newSection
    #         newCourse.isRequiredToDispaly = False
    #         newCourse.id = None
    #         newCourse.save()

    return render_to_response(
        'home.html',
        {},
        context_instance=RequestContext(request)
    )

@login_required
def uploadFile(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploadFilename = "%s.%s" % (uuid.uuid4(), ".html")
            newdoc = open(uploadFilename, "wb")
            data = request.FILES['docfile'];
            newdoc.write(data.read())
            Document(docfile=newdoc)
            newdoc.close()
            request.session["uploadFilename"] = uploadFilename

            return HttpResponseRedirect(reverse('myproject.myapp.views.selectProgram'))
    else:
        form = DocumentForm()  

    documents = '' #Document.objects.all()

    return render_to_response(
        'uploadFile.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

@login_required
def cloneProgram(request):
    if request.method == 'POST':
        programs_list = request.POST.getlist('programs')
        newTemplateName = request.POST.get('newTemplateName')
        url = reverse('myproject.myapp.views.cloneProgram')
        if len(programs_list) != 1 or len(newTemplateName) == 0 :
            return HttpResponseRedirect(url)

        try:
            x = Program.objects.get(programTitle=newTemplateName)
        except Program.DoesNotExist:
            x = None
        if x == None:    
            program = Program.objects.get(id=programs_list[0])
            newProgram = deepcopy(program)
            newProgram.programTitle = newTemplateName
            newProgram.id = None
            newProgram.save()
            sections = UnderOrGraduateSection.objects.filter(program=program)
            for section in sections:
                newSection = deepcopy(section)
                newSection.program = newProgram
                newSection.id = None
                newSection.save()
                courses = UnderOrGraduateCourse.objects.filter(section=section)
                for course in courses:
                    newCourse = deepcopy(course)
                    newCourse.section = newSection
                    newCourse.id = None
                    newCourse.save()

            if program.isGraduateProgram == True:
                areas = EmphasisArea.objects.filter(program=program)
                for area in areas:
                    newArea = deepcopy(area)
                    newArea.program = newProgram
                    newArea.id = None
                    newArea.save()
                    courses = EmphasisAreaCourse.objects.filter(emphasisArea=area)
                    for course in courses:
                        newCourse = deepcopy(course)
                        newCourse.emphasisArea = newArea
                        newCourse.id = None
                        newCourse.save()

        return HttpResponseRedirect(url)
    programs = Program.objects.all()
    return render_to_response(
        'cloneProgram.html',
        {'programs': programs},
        context_instance=RequestContext(request)
    )  

@login_required
def selectProgram (request):
    graduatePrograms = Program.objects.filter(isGraduateProgram=True)
    underGraduatePrograms = Program.objects.filter(isGraduateProgram=False)

    urlOfSelectEmphasis = reverse('myproject.myapp.views.selectEmphasis')
    urlOfSelectSection = reverse('myproject.myapp.views.selectSection')

    return render_to_response(
        'selectProgram.html',
        {'graduatePrograms': graduatePrograms, 'urlOfSelectEmphasis' : urlOfSelectEmphasis,
        'underGraduatePrograms': underGraduatePrograms, 'urlOfSelectSection' : urlOfSelectSection},
        context_instance=RequestContext(request)
    )

@login_required
def selectSection (request):
    programSelected = request.GET.get('programSelected', '')
    request.session["programSelected"] = programSelected
    print(programSelected)

    if request.method == 'POST':
        section_list = request.POST.getlist('sections')
        request.session['section_list'] = section_list
        url = reverse('myproject.myapp.views.viewTranscript')
        return HttpResponseRedirect(url)
    program = Program.objects.get(programTitle=programSelected)
    sections = UnderOrGraduateSection.objects.order_by('sectionId').filter(program=program)
    return render_to_response(
        'selectSection.html',
        {'sections': sections},
        context_instance=RequestContext(request)
    )

@login_required
def viewTranscript(request):
    uploadFilename = request.session["uploadFilename"]
    programSelected = request.session["programSelected"]
    student = Student()
    extractData.getDataList(student, uploadFilename)
    fo = open("file.json", "wb")
    fo.write(json.dumps(student.reprJSON(), cls=ComplexEncoder))
    fo.close()  
    # os.remove(uploadFilename)
    print(json.dumps(student.reprJSON(), cls=ComplexEncoder))

    programT = ProgramTemplate(programSelected,student.name)
    section_list = request.session['section_list']

    numOfSection = 0;
    restOfSections = []

    for index in section_list:
        section = UnderOrGraduateSection.objects.get(id = index)
        courses = UnderOrGraduateCourse.objects.order_by('courseId').filter(section = section)
        sectionT = SectionTemplate(section.sectionTitle, section.numOfRowToDisplay)
        i = 0
        for course in courses:
            # print (course.courseId)
            courseT =  CourseTemplate(course.courseTitle,course.courseId,course.creditHour)
            if sectionT.numOfRowToDisplay > i :
                extractData.fillData(student,courseT)
                if courseT.grade != "" or course.isRequiredToDispaly == True:
                    sectionT.courses.append(courseT)
                    i = i + 1
        if sectionT.numOfRowToDisplay != None and sectionT.numOfRowToDisplay > i :
            i = sectionT.numOfRowToDisplay - i
            for x in xrange(i):
                courseT =  CourseTemplate()
                sectionT.courses.append(courseT)
        numOfSection = numOfSection + 1
        if numOfSection < 6 :
            programT.sections.append(sectionT)
        else :
            restOfSections.append(sectionT)

    sectionT = SectionTemplate("Others", 0)
    for grade in student.gradeList:
        if grade.isListed == False:
            courseT =  CourseTemplate(grade.course_title, grade.department + grade.course_num,grade.creditHour)
            courseT.grade = grade.grade
            strList = grade.semester_completed.split(' ',3)
            courseT.semester = strList[0]
            if len(strList)>1:
                courseT.year = strList[1]
            else :
                courseT.year = strList[0]            
            sectionT.courses.append(courseT)
    restOfSections.append(sectionT)

    return render_to_response(
        'viewTranscript.html',
        {'program': programT,'restOfSections':restOfSections},
        context_instance=RequestContext(request)
    )

@login_required
def selectEmphasis (request):


    programSelected = request.GET.get('programSelected', '')
    request.session["programSelected"] = programSelected
    print(programSelected)

    if request.method == 'POST':
        selectedArea = request.POST.getlist('emphasisAreas')
        request.session['selectedArea'] = selectedArea
        url = reverse('myproject.myapp.views.viewGTranscript')
        return HttpResponseRedirect(url)

    program = Program.objects.get(programTitle=programSelected)
    emphasisAreas = EmphasisArea.objects.filter(program=program)
    return render_to_response(
        'selectEmphasis.html',
        {'emphasisAreas': emphasisAreas},
        context_instance=RequestContext(request)
    )

@login_required
def viewGTranscript(request):
    uploadFilename = request.session["uploadFilename"]
    programSelected = request.session["programSelected"]
    selectedAreaId = request.session['selectedArea']

    
    student = Student()
    extractData.getDataList(student, uploadFilename)
    fo = open("file.json", "wb")
    fo.write(json.dumps(student.reprJSON(), cls=ComplexEncoder))
    fo.close()  
    # os.remove(uploadFilename)
    print(json.dumps(student.reprJSON(), cls=ComplexEncoder))

    programT = ProgramTemplate(programSelected,student.name)

    program = Program.objects.get(programTitle=programSelected)
    sections = UnderOrGraduateSection.objects.filter(program=program)
    emphasisAreas = EmphasisArea.objects.filter(program=program)
    restOfSections = []

    for section in sections:

        if section.sectionId == 4:
            area = EmphasisArea.objects.get(id=selectedAreaId[0])
            courses = EmphasisAreaCourse.objects.filter(emphasisArea=area)
        else :
            courses = UnderOrGraduateCourse.objects.filter(section = section)
        sectionT = SectionTemplate(section.sectionTitle, section.numOfRowToDisplay)

        if section.sectionId == 5:
            electSection = section
            electCourses = courses
            continue

        i = 0
        for course in courses:
            courseT =  CourseTemplate(course.courseTitle,course.courseId,course.creditHour)
            if sectionT.numOfRowToDisplay > i :
                extractData.fillData(student,courseT)
                if courseT.grade != "" or course.isRequiredToDispaly == True:
                    sectionT.courses.append(courseT)
                    i = i + 1

        if section.sectionId == 1:
            prerequisiteSection = sectionT
            continue
        
        if sectionT.numOfRowToDisplay != None and sectionT.numOfRowToDisplay > i :
            i = sectionT.numOfRowToDisplay - i
            for x in xrange(i):
                courseT =  CourseTemplate()
                sectionT.courses.append(courseT)

        if section.sectionId == 2:
            programT.sections.append(sectionT)
        elif section.sectionId == 3:
            programT.sections.append(sectionT)
        elif section.sectionId == 4:
           selectedArea = sectionT
        else :
            restOfSections.append(sectionT)

    electSectionT = SectionTemplate(electSection.sectionTitle, electSection.numOfRowToDisplay)
    for grade in student.gradeList:
        if grade.isListed == True:
            continue
        if isInSection(grade,electCourses) == False:
            continue        
        courseT =  CourseTemplate(grade.course_title, grade.department + grade.course_num,grade.creditHour)
        courseT.grade = grade.grade
        strList = grade.semester_completed.split(' ',3)
        courseT.semester = strList[0]
        if len(strList)>1:
            courseT.year = strList[1]
        else :
            courseT.year = strList[0]            
        electSectionT.courses.append(courseT)
    
    i = electSectionT.numOfRowToDisplay - len(electSectionT.courses)
    if i > 0 :
        for x in xrange(i):
            courseT =  CourseTemplate()
            electSectionT.courses.append(courseT)

    return render_to_response(
        'viewGTranscript.html',
        {'program': programT, 'prerequisiteSection': prerequisiteSection, 
        'electSectionT': electSectionT, 'restOfSections': restOfSections,
        'emphasisAreas':emphasisAreas,'selectedArea': selectedArea},
        context_instance=RequestContext(request)
    )

def isInSection(grade,electCourses):
    courseId = grade.department + grade.course_num
    for course in electCourses:
        if courseId == course.courseId :
            return True

    return False
