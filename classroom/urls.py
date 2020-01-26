from django.urls import path
from classroom import views
from classroom.views import *


urlpatterns = [
	path('', HomePage.as_view()),
	path('classrooms/', ClassRoomsListView.as_view()),
	path('students/', StudentsView.as_view()),
]
