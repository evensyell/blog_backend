from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "update", "标签", "abstract", "markdown")

    def 标签(self, obj):
        return [a.tag_name for a in obj.tags.all()]


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    display = "tag_name"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    display = "__all__"


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    display = "__all__"

@admin.register(Hito)
class HitoAdmin(admin.ModelAdmin):
    display = "__all__"

@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    display = "__all__"

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    display = "__all__"