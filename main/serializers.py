from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Course, Lesson, UserCourses, UserLessons, UserClasses ,UserProfile, Class

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email','firstName', 'lastName')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'numOfLesson', 'name', 'link', 'assignment', 'course') 

class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'lessons')


class UserCoursesSerializer(serializers.ModelSerializer):
    # course = CourseSerializer(many=False)
    class Meta:
        model = UserCourses
        fields = ('id', 'user', 'numOfLesson', 'course')

class UserLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessons
        fields = ('id', 'user', 'answer','notes', 'lesson')
class UserClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClasses
        fields = ('id', 'classname', 'numberofstudents')  

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'className')  

class UserProfileSerializer(serializers.ModelSerializer):
    studentClasses = ClassSerializer(many=True)
    teacherClasses = ClassSerializer(many=True)
    coordinatorClasses = ClassSerializer(many=True)
    
    class Meta:
        model = UserProfile
        fields = ('id', 'user','username', 'firstName', 'lastName', 'aboutMe', 'hobbies', 'badges', 'myGoal',
         'studentClasses','teacherClasses', 'coordinatorClasses' )
    

                            