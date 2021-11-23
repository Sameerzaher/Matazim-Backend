from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.models import User 
from .serializers import UserSerializer, CourseSerializer, LessonSerializer, UserCoursesSerializer, UserLessonsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course, Lesson, UserCourses, UserLessons

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (AllowAny,)
    @action (detail=true, methods = ['POST'])
    def getuser(self, request, pk=None):
        user = User.object.get(id=pk)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer    

class UserCoursesViewSet(viewsets.ModelViewSet):
    queryset = UserCourses.objects.all()
    serializer_class = UserCoursesSerializer 

class UserLessonsViewSet(viewsets.ModelViewSet):
    queryset = UserLessons.objects.all()
    serializer_class = UserLessonsSerializer     