from django.conf import settings
from django.conf.urls import static, url
from django.contrib import admin
from django.urls import include, path

# from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.views import *
from users.views import *
from bbs.views import *


from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register("article", ArticleViewSet)
router.register("tag", TagViewSet)
router.register("music", MusicViewSet)
router.register("comment", CommentViewSet)
router.register("userpro", UserProViewSet)
router.register("post", PostViewSet)
router.register("reply", ReplyViewSet)

# 一般不去动下面
urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-register/", csrf_exempt(Register.as_view()), name="register"),
    # JWT token请求
    path("api/token/", TokenObtainPairView.as_view(), name="get_token",),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token",),
    path("djadmin/", admin.site.urls),
    # 静态资源/媒体资源访问
    url(
        r"^djstatic/(?P<path>.*)$",
        static.serve,
        {"document_root": settings.STATIC_ROOT},
        name="djstatic",
    ),
    url(r"^media/(?P<path>.*)$", static.serve, {"document_root": settings.MEDIA_ROOT},),
]
