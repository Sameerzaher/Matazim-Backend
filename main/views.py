from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.models import User 
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = (AllowAny,)
    # @action (detail=true, methods = ['POST'])
    # def getuser(self, request, pk=None):
    #     user = User.object.get(id=pk)