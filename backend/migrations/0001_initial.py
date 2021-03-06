# Generated by Django 3.0.4 on 2021-06-04 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('share', models.BooleanField(blank=True, default=False)),
                ('img', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/img/article_img/')),
                ('markdown', models.FileField(blank=True, upload_to='%Y/markdown/')),
                ('update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-update',),
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.FileField(upload_to='%Y/music/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('artist', models.CharField(blank=True, max_length=100)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-update',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, unique=True, verbose_name='标签名')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='backend.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='backend.Tag'),
        ),
    ]
