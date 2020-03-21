# Generated by Django 3.0.4 on 2020-03-21 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200317_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(max_length=200, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='software',
            name='abstract',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='video',
            name='abstract',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
    ]