from rest_framework import serializers

from evens.settings import MEDIA_ROOT

from .models import *
from .tools import *


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # imgs = serializers.ListField(
    #     child=serializers.FileField(allow_empty_file=False),
    #     write_only=True,
    #     required=False,
    # )
    # img = serializers.ImageField(read_only=True)

    class Meta:
        model = Img
        fields = "__all__"

    def create(self, validated_data):
        if "img" in validated_data:
            img_data = validated_data.pop("img")
            # for img_data in imgs_data:
            md5 = GetMd5(img_data)
            img, crated = Img.objects.get_or_create(md5=md5)
            if crated:
                img.img = img_data
                img.save()
        return img


class HitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hito
        fields = "__all__"


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"

    def create(self, validated_data):
        data = validated_data.pop("music")
        music = Music.objects.create(music=data)
        (filepath, tempfilename) = os.path.split(music.music.name)
        (filename, extension) = os.path.splitext(tempfilename)
        (artist, title) = filename.split("_-_")

        a = artist.replace("_", " ")
        b = title.replace("_", " ")
        (music.artist, music.title) = (a, b)

        music.save()
        return music


class ImageUrlField(serializers.RelatedField):
    def to_representation(self, instance):
        url = instance.img.url
        request = self.context.get("request", None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tag = serializers.ListField(write_only=True, required=False)
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="tag_name", required=False
    )

    class Meta:
        model = Article
        fields = "__all__"

    def create(self, validated_data):
        if "tag" in validated_data:
            tags_data = validated_data.pop("tag")
            article = Article.objects.create(**validated_data)
            for tag_data in tags_data:
                tag, crated = Tag.objects.get_or_create(tag_name=tag_data)
                article.tags.add(tag)
        else:
            article = Article.objects.create(**validated_data)
        return article


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    imgs = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False),
        write_only=True,
        required=False,
    )
    software_imgs = ImageUrlField(many=True, read_only=True)

    class Meta:
        model = Software
        fields = "__all__"

    def create(self, validated_data):
        if "imgs" in validated_data:
            imgs_data = validated_data.pop("imgs")
            software = Software.objects.create(**validated_data)
            for img_data in imgs_data:
                md5 = GetMd5(img_data)
                img, crated = Img.objects.get_or_create(md5=md5)
                if crated:
                    img.software = software
                    img.img = img_data
                    img.save()
                else:
                    img.software = software
                    img.save()
        else:
            software = Software.objects.create(**validated_data)
        return software

    # 展示choices的value，而不是key
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(os=instance.get_os_display())
        return data


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    imgs = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False),
        write_only=True,
        required=False,
    )
    video_imgs = ImageUrlField(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"

    def create(self, validated_data):
        if "imgs" in validated_data:
            imgs_data = validated_data.pop("imgs")
            video = Video.objects.create(**validated_data)
            for img_data in imgs_data:
                md5 = GetMd5(img_data)
                img, crated = Img.objects.get_or_create(md5=md5)
                if crated:
                    img.video = video
                    img.img = img_data
                    img.save()
                else:
                    img.video = video
                    img.save()
        else:
            video = Video.objects.create(**validated_data)
        return video

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(category=instance.get_category_display())
        return data
