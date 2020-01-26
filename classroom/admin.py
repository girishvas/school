from django.contrib import admin
from .models import *


class SubjectAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'perClassDuration', 'totalDuration', 'createdOn')
	list_filter 	= ['createdOn']
	search_fields 	= ['name']

	# def class_rooms(self, obj):
		# return ', '.join(map(lambda x: x.name, list(obj.classes.all())))

admin.site.register(Subject, SubjectAdmin)


class ClassRoomAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'capacity', 'webSupport', 'shape', 'subjects_in_class', 'createdOn')
	list_filter 	= ['createdOn', 'webSupport', 'shape']
	search_fields 	= ['name', 'shape', 'subjects']

	def subjects_in_class(self, obj):
		return ', '.join(map(lambda x: x.name, list(obj.subjects.all())))

admin.site.register(ClassRoom, ClassRoomAdmin)


class StudentAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'doj', 'standard', 'rollNo', 'ranking', 'class_rooms', 'createdOn')
	list_filter 	= ['createdOn', 'standard']
	search_fields 	= ['name']

	def class_rooms(self, obj):
		return ', '.join(map(lambda x: x.name, list(obj.classes.all())))

admin.site.register(Student, StudentAdmin)


class StudentContactAdmin(admin.ModelAdmin):
	list_display 	= ('contactName', 'contactNumber', 'relation', 'student', 'createdOn')
	list_filter 	= ['createdOn', 'student']
	search_fields 	= ['contactName', 'contactNumber', 'relation', 'student']

admin.site.register(StudentContact, StudentContactAdmin)


class ChapterAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'subject', 'order', 'createdOn')
	list_filter 	= ['createdOn']
	search_fields 	= ['name']

admin.site.register(Chapter, ChapterAdmin)


class TeacherAdmin(admin.ModelAdmin):
	list_display 	= ('name', 'webSupport', 'doj', 'annualSalary', 'subjects_handling', 'createdOn')
	list_filter 	= ['createdOn', 'webSupport']
	search_fields 	= ['name']

	def subjects_handling(self, obj):
		return ', '.join(map(lambda x: x.name, list(obj.subjects.all())))

admin.site.register(Teacher, TeacherAdmin)


class ClassroomSubjectAdmin(admin.ModelAdmin):
	list_display 	= ('classroom', 'teacher', 'createdOn')
	list_filter 	= ['createdOn']
	search_fields 	= ['classroom', 'teacher']


admin.site.register(ClassroomSubject, ClassroomSubjectAdmin)