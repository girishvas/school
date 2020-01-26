from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


shape = [
	('oval', 'Oval'), 
	('rectangular', 'Rectangular'), 
	('canopy', 'Canopy'), 
	('elevated', 'Elevated')
]

class Subject(models.Model):
	name 			= models.CharField(max_length=200)
	perClassDuration= models.IntegerField(validators=[MaxValueValidator(120), MinValueValidator(30)])
	totalDuration 	= models.IntegerField()

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ClassRoom(models.Model):
	name 			= models.CharField(max_length=200)
	capacity 		= models.IntegerField()
	webSupport 		= models.BooleanField()
	shape 			= models.CharField(max_length=50, choices=shape)
	subjects 		= models.ManyToManyField(Subject, through='ClassroomSubject')

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Student(models.Model):
	name 			= models.CharField(max_length=200)
	doj 			= models.DateField()
	standard 		= models.IntegerField()
	rollNo 			= models.IntegerField()
	ranking 		= models.IntegerField()
	classes 		= models.ManyToManyField(ClassRoom)

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class StudentContact(models.Model):
	contactName 	= models.CharField(max_length=200)
	contactNumber 	= models.CharField(max_length=200)
	relation 		= models.CharField(max_length=200)
	student 		= models.ForeignKey(Student, on_delete=models.CASCADE)

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)    

	def __str__(self):
		return self.contactName


class Chapter(models.Model):
	name 			= models.CharField(max_length=300)
	order 			= models.IntegerField()
	subject 		= models.ForeignKey(Subject, on_delete=models.PROTECT)

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Teacher(models.Model):
	name 			= models.CharField(max_length=200)
	doj 			= models.DateField()
	subjects 		= models.ManyToManyField(Subject)
	webSupport 		= models.BooleanField()
	annualSalary 	= models.FloatField()

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class ClassroomSubject(models.Model):
	classroom 		= models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
	subject 		= models.ForeignKey(Subject, on_delete=models.PROTECT)
	teacher 		= models.ForeignKey(Teacher, on_delete=models.PROTECT)

	createdOn 		= models.DateTimeField(auto_now_add=True, null=True)
	updatedOn 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} ({})'.format(self.classroom, self.subject)

	def clean(self):
		if self.subject not in self.teacher.subjects.all():
			raise ValidationError("Invalid teacher selected, {} is not able to teach {}".format(self.teacher, self.subject))