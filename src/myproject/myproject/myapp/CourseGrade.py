import json

class CourseGrade:
    def __init__(self, department = None, course_num = None ,course_title = None ,grade = None, semester_completed = None, creditHour = None, isListed = False):
        self.department = department
        self.course_title = course_title
        self.course_num = course_num
        self.grade = grade
        self.semester_completed = semester_completed
        self.creditHour =creditHour
        self.isListed = isListed

    def reprJSON(self):
        return dict(department = self.department, course_num = self.course_num ,course_title = self.course_title ,grade = self.grade, semester_completed = self.semester_completed)

class Student:
    def __init__(self, name = None, sId = None):
        self.name = name
        self.sId = sId
        self.gradeList = []

    def reprJSON(self):
        return dict(name=self.name, sId=self.sId, gradeList=self.gradeList)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

class ProgramTemplate:
    def __init__(self, programTitle = None, studentName = None , section = None):
        self.programTitle = programTitle
        self.studentName = studentName
        self.sections = []

class SectionTemplate:
    def __init__(self, sectionTitle = None, numOfRowToDisplay = None , courses = None):
        self.sectionTitle = sectionTitle
        self.numOfRowToDisplay = numOfRowToDisplay
        self.courses = []

class CourseTemplate:
    def __init__(self, courseTitle = "", courseId = "", creditHour = "", grade = "", semester = "", year = ""):
        self.courseTitle = courseTitle
        self.courseId = courseId
        self.creditHour = creditHour
        self.grade = grade
        self.semester = semester
        self.year = year

