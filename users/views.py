from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import viewsets

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class UserProViewSet(viewsets.ModelViewSet):
    queryset = UserPro.objects.all()
    serializer_class = UserProSerializer
