import os
from .models import *
from evens import settings
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User  # django封装好的验证功能


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "pro__nickname", "is_superuser")


class UserProSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    is_superuser = serializers.BooleanField(source="user.is_superuser", read_only=True)

    class Meta:
        model = UserPro
        fields = "__all__"
        depth = 3

    def update(self, instance, validated_data):
        if "avatar" in validated_data:
            if instance.avatar:
                old_file = os.path.join(settings.MEDIA_ROOT, instance.avatar.path)
                if old_file:
                    os.remove(old_file)
            instance.avatar = validated_data.get("avatar", instance.avatar)
            instance.nickname = validated_data.get("nickname", instance.nickname)
            instance.motoo = validated_data.get("motoo", instance.motoo)

        instance.save()
        return instance