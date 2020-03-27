from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from evens.settings import MEDIA_URL

MEDIA_URL = MEDIA_URL.replace("\\", "/")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "update",
        "标签",
        "abstract",
        "image_data",
        "markdown",
    )
    filter_horizontal = ["tags"]

    def image_data(self, obj):
        # 使用mark_safe返回内容，否则页面将以html实体展示输出结果
        return mark_safe(
            '<img src="%s/%s" width="100px",style:"overflow:auto;height:100px">'
            % (MEDIA_URL, obj.img)
        )

    def 标签(self, obj):
        return [tag.tag_name for tag in obj.tags.all()]


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
