from django.contrib import admin
from .models import Course, Lesson, UserCourses, UserLessons, UserClasses , UserProfile, Class
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(UserCourses)
admin.site.register(UserLessons)
admin.site.register(UserClasses)
admin.site.register(UserProfile)
admin.site.register(Class)