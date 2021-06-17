import os

from django.contrib.auth.models import User  # django封装好的验证功能
from evens import settings
from rest_framework import serializers
from users.serializers import *

from .models import *
from .tools import *


# from django.core.files.storage import default_storage
def titileFromPath(path):
    print("---------------------------")
    print(path)
    (filepath, tempfilename) = os.path.split(path)
    (filename, extension) = os.path.splitext(tempfilename)

    print("---------------------------")
    return filename.split("_")[0]  # 去掉唯一化后缀


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Music
        fields = "__all__"

    def create(self, validated_data):
        music = Music.objects.create(**validated_data)
        (filepath, tempfilename) = os.path.split(music.music.name)
        (filename, extension) = os.path.splitext(tempfilename)
        (artist, title) = filename.split("_-_")

        a = artist.replace("_", " ")
        b = title.replace("_", " ")
        (music.artist, music.title) = (a, b)

        music.save()
        return music


class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source="user.pro.nickname", read_only=True)
    user_avatar = serializers.ImageField(source="user.pro.avatar", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tag = serializers.ListField(write_only=True, required=False)
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="tag_name", required=False
    )
    comments = CommentSerializer(many=True, read_only=True, required=False)

    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # author = serializers.IntegerField(write_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        if "tag" in validated_data:
            tags_data = validated_data.pop("tag")
            article = Article.objects.create(**validated_data)

            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(tag_name=tag_data)
                article.tags.add(tag)
        else:
            article = Article.objects.create(**validated_data)

        article.title = titileFromPath(article.markdown.name)
        article.save()

        return article

    def update(self, instance, validated_data):
        if "tag" in validated_data:
            tags_data = validated_data.pop("tag")
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(tag_name=tag_data)
                instance.tags.add(tag)

        if "img" in validated_data:
            if instance.img:
                old_file = os.path.join(settings.MEDIA_ROOT, instance.img.path)
                if old_file:
                    os.remove(old_file)
            instance.img = validated_data.get("img", instance.img)

        if "markdown" in validated_data:
            if instance.markdown:
                old_file = os.path.join(settings.MEDIA_ROOT, instance.markdown.path)
                if old_file:
                    os.remove(old_file)
            instance.markdown = validated_data.get("markdown", instance.markdown)
            instance.title = titileFromPath(instance.markdown.name)
        instance.save()
        return instance


class TagSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ("id", "tag_name", "article_set")


# class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     imgs = serializers.ListField(
#         child=serializers.FileField(allow_empty_file=False),
#         write_only=True,
#         required=False,
#     )
#     software_imgs = ImageUrlField(many=True, read_only=True)

#     class Meta:
#         model = Software
#         fields = "__all__"

#     def create(self, validated_data):
#         if "imgs" in validated_data:
#             imgs_data = validated_data.pop("imgs")
#             software = Software.objects.create(**validated_data)
#             for img_data in imgs_data:
#                 md5 = GetMd5(img_data)
#                 img, crated = Img.objects.get_or_create(md5=md5)
#                 if crated:
#                     img.software = software
#                     img.img = img_data
#                     img.save()
#                 else:
#                     img.software = software
#                     img.save()
#         else:
#             software = Software.objects.create(**validated_data)
#         return software

#     # 展示choices的value，而不是key
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data.update(os=instance.get_os_display())
#         return data


# class ImgSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Img
#         fields = "__all__"

#     def create(self, validated_data):
#         if "img" in validated_data:
#             img_data = validated_data.pop("img")
#             # for img_data in imgs_data:
#             md5 = GetMd5(img_data)
#             img, crated = Img.objects.get_or_create(md5=md5)
#             if crated:
#                 img.img = img_data
#             img.save()
#         return img

# class ImageUrlField(serializers.RelatedField):
#     def to_representation(self, instance):
#         url = instance.img.url
#         request = self.context.get("request", None)
#         if request is not None:
#             return request.build_absolute_uri(url)
#         return url
