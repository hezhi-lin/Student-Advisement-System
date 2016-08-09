# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

class Program(models.Model):
    programTitle = models.CharField(max_length=255)
    isGraduateProgram = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.programTitle)
    class Meta:        
        unique_together = (("programTitle"),)

class UnderOrGraduateSection(models.Model):
    program = models.ForeignKey(Program)
    sectionId = models.IntegerField()
    sectionTitle = models.CharField(max_length=255)
    numOfRowToDisplay = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.program.programTitle, self.sectionTitle)

    def get_program(self):
        return self.program.programTitle
    get_program.short_description = 'Program'

    class Meta:
            unique_together = (("program", "sectionId"),)

class UnderOrGraduateCourse(models.Model):

    courseId = models.CharField(max_length=255)
    courseTitle = models.CharField(max_length=255)
    isRequiredToDispaly = models.BooleanField(default=False)
    creditHour = models.IntegerField(default=3)
    section = models.ForeignKey(UnderOrGraduateSection)

    def get_program(self):
        return self.section.get_program()
    get_program.short_description = 'Program'

    def get_sectionTitle(self):
        return self.section.sectionTitle
    get_sectionTitle.short_description = 'Section Title'

    def get_sectionId(self):
        return self.section.sectionId
    get_sectionId.short_description = 'Section Id'

    class Meta:
            unique_together = (("courseId", "section"),)


class EmphasisArea(models.Model):
    program = models.ForeignKey(Program)
    emphasisAreaId = models.CharField(max_length=255)
    emphasisAreaTitle = models.CharField(max_length=255)
    numOfRowToDisplay = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.program.programTitle, self.emphasisAreaId, self.emphasisAreaTitle)

    def get_program(self):
        return self.program.programTitle
    get_program.short_description = 'Program'

    class Meta:
            unique_together = (("program", "emphasisAreaId"),)


class EmphasisAreaCourse(models.Model):

    courseId = models.CharField(max_length=255)
    courseTitle = models.CharField(max_length=255)
    isRequiredToDispaly = models.BooleanField(default=False)
    creditHour = models.IntegerField(default=3)
    emphasisArea = models.ForeignKey(EmphasisArea)

    def __str__(self):
        return '%s  Course ID:%s  CourseTitle:%s  is required to display:%s  Credit Hour:%s ' \
        % (self.emphasisArea, self.courseId, self.courseTitle, self.isRequiredToDispaly, self.creditHour)

    def get_program(self):
        return self.emphasisArea.get_program()
    get_program.short_description = 'Program'

    def get_emphasisAreaTitle(self):
        return self.emphasisArea.emphasisAreaTitle
    get_emphasisAreaTitle.short_description = 'Emphasis Area Title'

    def get_emphasisAreaId(self):
        return self.emphasisArea.emphasisAreaId
    get_emphasisAreaId.short_description = 'Emphasis Area'

    class Meta:
            unique_together = (("courseId", "emphasisArea"),)


