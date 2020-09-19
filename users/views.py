from django.shortcuts import render

from django.contrib.auth.models import User  # django封装好的验证功能
from django.views import View
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework.parsers import *
from django.contrib import auth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class UserProViewSet(viewsets.ModelViewSet):
    queryset = UserPro.objects.all()
    serializer_class = UserProSerializer
    filterset_fields = [
        "user__username",
    ]


# class Login(View):
#     def post(self, request):
#         try:
#             user = request.POST.get("username", None)
#             pwd = request.POST.get("password", None)
#             # 验证密码
#             obj = auth.authenticate(request, username=user, password=pwd)
#             if obj:
#                 return JsonResponse({"code": "ok", "message": "账号密码验证成功"})
#         except:
#             return JsonResponse({"code": "no", "message": "验证失败"})


class Register(View):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except:
            return JsonResponse({"code": "no", "message": "注册失败"})
        return JsonResponse({"code": "ok", "message": "注册成功"})
