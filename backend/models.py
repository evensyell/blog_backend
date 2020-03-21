import os
from time import strftime

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Tag(models.Model):
    tag_name = models.CharField("标签名", max_length=20, unique=True)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField("标题", max_length=90)
    abstract = models.CharField("摘要", max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    img = ProcessedImageField(upload_to="%Y/img/article_img/", blank=True)
    markdown = models.FileField(upload_to="%Y/markdown/", blank=True)
    update = models.DateTimeField(auto_now=True,)

    class Meta:
        ordering = ("-update",)

    def __str__(self):
        return self.title


class Software(models.Model):
    OS_CHOICES = ((1, "Windows"), (2, "Android"), (3, "Chrome"))

    title = models.CharField("软件名", max_length=90)
    version = models.CharField("版本号", max_length=10)
    os = models.IntegerField("平台", choices=OS_CHOICES)
    abstract = models.CharField("简介", max_length=200)
    logo = ProcessedImageField(upload_to="%Y/img/software_logo/", blank=True)
    update = models.DateTimeField(auto_now=True)
    link1 = models.CharField(max_length=9999, blank=True)
    link2 = models.CharField(max_length=9999, blank=True)
    link3 = models.CharField(max_length=9999, blank=True)

    class Meta:
        ordering = ("-update",)

    def __str__(self):
        return self.title


class Video(models.Model):
    CATEGORY_CHOICES = ((1, "Anime"), (2, "Movie"), (3, "Dorama"), (4, "Chip"))

    title = models.CharField("标题", max_length=90)
    abstract = models.CharField("简介", max_length=200)
    category = models.IntegerField("类型", choices=CATEGORY_CHOICES)
    sub = models.CharField("字幕", max_length=10)
    cover = ProcessedImageField(upload_to="%Y/img/video_cover/", blank=True)
    link1 = models.CharField(max_length=9999, blank=True)
    link2 = models.CharField(max_length=9999, blank=True)
    link3 = models.CharField(max_length=9999, blank=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-update",)

    def __str__(self):
        return self.title


class Img(models.Model):
    img = models.ImageField(upload_to="%Y/img/", blank=True)
    md5 = models.CharField(max_length=128, unique=True, blank=True)
    software = models.ForeignKey(
        Software,
        related_name="software_imgs",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    video = models.ForeignKey(
        Video,
        related_name="video_imgs",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.md5

    class Meta:
        ordering = ("-pk",)


class Hito(models.Model):
    what = models.CharField(max_length=999)
    who = models.CharField(max_length=64)
    where = models.CharField(max_length=64)

    def __str__(self):
        return self.what

    class Meta:
        ordering = ("-pk",)

class Music(models.Model):
    music = models.FileField(upload_to="%Y/music/")
    title = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-update",)
