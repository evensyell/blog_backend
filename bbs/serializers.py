import os

from django.contrib.auth.models import User  # django封装好的验证功能
from evens import settings
from rest_framework import serializers
from users.serializers import *

from .models import *

# from .tools import *


class ReplySerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source="author.pro.nickname", read_only=True)
    user_avatar = serializers.ImageField(source="author.pro.avatar", read_only=True)

    class Meta:
        model = Reply
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_nickname = serializers.CharField(source="author.pro.nickname", read_only=True)
    user_avatar = serializers.ImageField(source="author.pro.avatar", read_only=True)
    replies = ReplySerializer(many=True, read_only=True, required=False)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = "__all__"

    def update(self, instance, validated_data):
        if "markdown" in validated_data:
            if instance.markdown:
                old_file = os.path.join(settings.MEDIA_ROOT, instance.markdown.path)
                if old_file:
                    os.remove(old_file)
            instance.markdown = validated_data.get("markdown", instance.markdown)
        instance.save()
        return instance
