from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, CourseViewSet, LessonViewSet, UserCoursesViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('courses', CourseViewSet)
router.register('lessons', LessonViewSet)
router.register('userCourses', UserCoursesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]