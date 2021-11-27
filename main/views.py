from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.models import User 
from .serializers import UserSerializer, CourseSerializer, LessonSerializer, UserCoursesSerializer, UserLessonsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Course, Lesson, UserCourses, UserLessons
from rest_framework import status
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (AllowAny,)
    @action (detail=True, methods = ['POST'])
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
    authentication_classes = (TokenAuthentication, )
     
    #  Get all the userLessons details belonged to the requsted user by the authentication
    @action (detail=True, methods = ['GET'])
    def getUserLessons(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        arr=[]
        userlessons= UserLessons.objects.filter(user=user.id)
        for userlesson in userlessons:
             serializers = UserLessonsSerializer(userlesson, many=False)
             arr.append(serializers.data)
            
        response = {'message': 'Get', 'results': arr }
        return Response (response, status=status.HTTP_200_OK)

    #  Update or create a userLessons 
    @action (detail=True, methods = ['POST'])
    def addUserLessons(self, request, pk=None):
        # get the user by the authentication
        user = request.user
        # if getUserLessons get a value (len(getUserLessons) > 0) it means that 
        # this object exist in DB and the user is trying to update that object.
        getUserLessons= UserLessons.objects.filter(user=user.id, lesson=pk)       
                
        try:
            # success if need to update 
            lesson = UserLessons.objects.get(id=getUserLessons[0].id)
            print("printing: ",lesson.notes, lesson.answer)
            lesson.user = user
            # user trying to change the note
            if 'notes' in request.data:
                notes = request.data['notes']
                lesson.notes = notes
             # user trying to change the answer
            if 'answer' in request.data:
                answer = request.data['answer']
                lesson.answer = answer
            
            lesson.save()
            print ("user is: ", user)
            serializers = UserLessonsSerializer(lesson, many=False)
            response = {'message': 'Updated', 'results': serializers.data }
            return Response (response, status=status.HTTP_200_OK)
        except:
            # need to create
            print("trying to create")
            print("pk ", pk)
            # user trying to create a note
            if 'notes' in request.data:
                notes = request.data['notes']
                answer = ""
            # user trying to create an answer
            if 'answer' in request.data:
                answer = request.data['answer']
                notes = ""
               
            lesson = Lesson.objects.get(id=pk)
            lessonVar = UserLessons.objects.create(user=user,lesson=lesson, answer=answer, notes=notes )
            lessonVar.save()
            response = {'message': 'created', 'results': lessonVar }
            return Response (response, status=status.HTTP_200_OK)