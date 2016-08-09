from bs4 import BeautifulSoup
from CourseGrade import *

def splitTr(tr, grade):
    grade.department = tr.find_all('td')[0].text.lstrip()
    grade.course_num = tr.find_all('td')[1].text
    if tr.find_all('td')[2].text == "UG" or tr.find_all('td')[2].text == "GR":
        grade.course_title = tr.find_all('td')[3].text
        grade.grade = tr.find_all('td')[4].text.lstrip()
        grade.creditHour = int(float(tr.find_all('td')[5].text.lstrip()))
    else :
        grade.course_title = tr.find_all('td')[2].text
        grade.grade = tr.find_all('td')[3].text.lstrip()
        grade.creditHour = int(float(tr.find_all('td')[4].text.lstrip()))

def getDataList(student, fileName="Academic Transcript.html"):
    file = open(fileName,'r')
    soup = BeautifulSoup(file,"html.parser")
    
    studentName = soup.find("a", {"name":"Student Address"})
    if studentName != None:
        student.name = studentName.contents[0]
    else:
        studentName = soup.find("div","staticheaders").contents[0]
        student.name = studentName.split()[1]+ " " + studentName.split()[2]
    print(soup.find('td',attrs={'class':'dddefault','colspan':6}).contents[0])

    table = soup.find('table',attrs={'class':'datadisplaytable'})
    # print(table)
    # table_body = table.findAll('tbody')
    # print(table_body)
    trs = table.find_all('tr')
    count = 0
    term = ''
    department = ''
    course_title = ''
    grade = ''
    for tr in trs:
        if tr.find('span',attrs={'class':'fieldOrangetextbold'}):
            term = tr.span.text
            term = term.replace(":", "")
            term = term.replace("Term", "").lstrip()
            term = uniformTerm(term)
            continue
        if tr.find('td',attrs={'class':'dddefault','colspan':4}) or tr.find('td',attrs={'class':'dddefault','colspan':5}):
            grade = CourseGrade()
            splitTr(tr, grade)
            grade.semester_completed = term
            appendValidData(student, grade) 
            count = count + 1

def appendValidData(student, grade):
    if grade.grade == 'A':
        student.gradeList.append(grade)
    if grade.grade == 'B':
        student.gradeList.append(grade)
    if grade.grade == 'C':
        student.gradeList.append(grade)
    if grade.grade == 'P':
        student.gradeList.append(grade)
    if grade.grade == 'TA':
        student.gradeList.append(grade)
    if grade.grade == 'TB':
        student.gradeList.append(grade)
    if grade.grade == 'TC':
        student.gradeList.append(grade)
    if grade.grade == 'TP':
        student.gradeList.append(grade)

def fillData(student,courseT):
    for grade in student.gradeList:
        gradeId = grade.department + grade.course_num
        if gradeId == courseT.courseId :
                courseT.grade = grade.grade
                if grade.semester_completed != "":
                    strList = grade.semester_completed.split(' ',3)
                    courseT.semester = strList[0]
                    if len(strList)>1:
                        courseT.year = strList[1]
                    else :
                        courseT.year = strList[0]
                    grade.isListed = True


def uniformTerm(term):
    data = term
    print(data)
    if RepresentsInt(data):
        if len(data) == 6:
            year = data[0:4]
            semester = data[4:7]
            if semester == '20':
                semester = 'Spring'
            elif semester == '30':
                semester = 'Summer'
            elif semester == '40':
                semester = 'Fall'
            else :
                semester = 'None'
            term = semester + " " + year
    return term

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
