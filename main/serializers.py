from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Course, Lesson, UserCourses, UserLessons, UserClasses ,UserProfile

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

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user','username', 'email', 'firstName', 'lastName', 'aboutMe', 'hobbies')

                            