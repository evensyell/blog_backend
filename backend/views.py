from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import *

from .models import *
from .serializers import *


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "article": reverse("article-list", request=request, format=format),
            "tag": reverse("tag-list", request=request, format=format),
            "software": reverse(
                "software-list", request=request, format=format
            ),
            "video": reverse("video-list", request=request, format=format),
        }
    )


class ImgViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    parser_classes = (
        MultiPartParser,
        FileUploadParser,
    )


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "tags",
    ]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    filterset_fields = [
        "os",
    ]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filterset_fields = [
        "category",
    ]


class HitoViewSet(viewsets.ModelViewSet):
    queryset = Hito.objects.all()
    serializer_class = HitoSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
