from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *


class HomePage(View):
	def get(self, request, *args, **kwargs):
		teachers 			= Teacher.objects.filter(annualSalary__gt=12).aggregate(
			salary_sum=Sum('annualSalary', distinct=True),
			students_count=Count('classroomsubject__classroom__student', distinct=True)
		)
		sum_of_salaries 	= teachers['salary_sum']
		students 			= teachers['students_count']
		sum_of_salaries 	= Teacher.objects.filter(annualSalary__gt=12).aggregate(Sum('annualSalary'))['annualSalary__sum']

		subjects_report 	= Subject.objects.annotate(teachers_count=Count('teacher')).filter(teachers_count__gt=1).aggregate(
			students=Count('classroom__student', distinct=True),
			teachers=Count('teacher'),
			totalDuration=Sum('totalDuration')
		)
		no_of_students 		= subjects_report['students']
		no_of_teachers 		= subjects_report['teachers']
		total_duration 		= subjects_report['totalDuration']

		return render(request, "index.html", locals())


class ClassRoomsListView(View):
	def get(self, request, *args, **kwargs):
		room 			= ClassRoom.objects.all()
		return render(request, "classroom_list.html", locals())


class StudentsView(View):
	def get(self, request, *args, **kwargs):
		students 		= Student.objects.all()
		query = request.GET.get('q')
		if query:
			students 	= students.filter(classes__classroomsubject__teacher__name__icontains=query)
		else:
			query 		= ''
		return render(request, "std_list.html", locals())
