from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=360)

class Lesson(models.Model):
    numOfLesson = models.IntegerField()
    name = models.CharField(max_length=32)
    link = models.CharField(max_length=100)
    assignment = models.CharField(max_length=300)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons') 
    class meta:
        unique_together = (('numOfLesson', 'course'),) 
        index_together = (('numOfLesson', 'course'),) 

class UserCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    numOfLesson = models.IntegerField()
    class meta:
        unique_together = (('numOfLesson', 'course', 'user'),) 
        index_together = (('numOfLesson', 'course', 'user'),) 

class UserLessons(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
    notes =  models.CharField(max_length=400)
    class meta:
        unique_together = (( 'lesson', 'user'),) 
        index_together = (( 'lesson', 'user'),) 

class UserClasses(models.Model):
    
    ClassName = models.CharField(max_length=32)
    NumberOfStudents = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30)])
    
           