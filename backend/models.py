# import os
# from time import strftime
# from users.models import UserPro
from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User

# from mptt.models import MPTTModel, TreeForeignKey


class Tag(models.Model):
    tag_name = models.CharField("标签名", max_length=20, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ("id",)


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    special = models.BooleanField(blank=True, default=False)
    img = ProcessedImageField(upload_to="%Y/img/article_img/", blank=True)
    markdown = models.FileField(upload_to="%Y/markdown/", blank=True)
    update = models.DateTimeField(auto_now=True,)
    # userpro = models.ForeignKey(
    #     UserPro, on_delete=models.CASCADE, related_name="articles"
    # )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    class Meta:
        ordering = ("-update",)

    def __str__(self):
        return self.title


class Music(models.Model):
    music = models.FileField(upload_to="%Y/music/")
    title = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-update",)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.content[:20]
