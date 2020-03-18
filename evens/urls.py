from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from backend import views

router = DefaultRouter()
router.register("article", views.ArticleViewSet)
router.register("tag", views.TagViewSet)
router.register("software", views.SoftwareViewSet)
router.register("video", views.VideoViewSet)
router.register("img", views.ImgViewSet)
router.register("hito", views.HitoViewSet)
router.register("music", views.MusicViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
