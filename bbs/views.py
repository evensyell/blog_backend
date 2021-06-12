# from django.http import JsonResponse, HttpResponse
# from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.reverse import reverse

# from rest_framework.parsers import *
# from django.contrib.auth.models import User  # django封装好的验证功能

# from django.contrib import auth
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "post": reverse("post-list", request=request, format=format),
            # "tag": reverse("tag-list", request=request, format=format),
        }
    )


class MyNumberPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 10000


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = [
        "author",
    ]
    pagination_class = MyNumberPagination


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    filterset_fields = ["post", "author"]
    ordering_fields = ["id"]
