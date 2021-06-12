# from django.http import JsonResponse, HttpResponse
# from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from rest_framework.parsers import *
# from django.contrib.auth.models import User  # django封装好的验证功能
# from django.contrib import auth
from .models import *
from .serializers import *


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "article": reverse("article-list", request=request, format=format),
            "tag": reverse("tag-list", request=request, format=format),
        }
    )


class MyNumberPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    max_page_size = 10000


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["tags", "special"]
    pagination_class = MyNumberPagination


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ["article", "user"]
    ordering_fields = ["id", "created"]


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    # pagination_class = MyNumberPagination

