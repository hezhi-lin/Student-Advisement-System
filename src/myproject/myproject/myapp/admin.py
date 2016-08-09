from django.contrib import admin
from myproject.myapp.models import *
# Register your models here.
class UnderOrGraduateSectionAdmin(admin.ModelAdmin):
    list_display = ('get_program', 'sectionId', 'sectionTitle', 'numOfRowToDisplay')
class UnderOrGraduateCourseAdmin(admin.ModelAdmin):
    list_display = ('get_program' ,'get_sectionId', 'get_sectionTitle' , 'courseId', 'courseTitle', 'isRequiredToDispaly', 'creditHour')
class EmphasisAreaAdmin(admin.ModelAdmin):
    list_display = ('get_program', 'emphasisAreaId', 'emphasisAreaTitle', 'numOfRowToDisplay')
class EmphasisAreaCourseAdmin(admin.ModelAdmin):
    list_display = ('get_program' ,'get_emphasisAreaId', 'get_emphasisAreaTitle', 'courseId', 'courseTitle', 'isRequiredToDispaly', 'creditHour')
admin.site.register(Document)
admin.site.register(Program)
admin.site.register(EmphasisArea, EmphasisAreaAdmin)
admin.site.register(EmphasisAreaCourse, EmphasisAreaCourseAdmin)
admin.site.register(UnderOrGraduateSection, UnderOrGraduateSectionAdmin)
admin.site.register(UnderOrGraduateCourse, UnderOrGraduateCourseAdmin)