from django.db import models
import os

# from users.models import UserPro
from imagekit.models import ProcessedImageField

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=900, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now=True,)
    # userpro = models.ForeignKey(
    #     UserPro, on_delete=models.CASCADE, related_name="articles"
    # )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    img = ProcessedImageField(upload_to="img/post_img/", blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.content[:20]
