# Generated by Django 3.0.4 on 2020-03-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200322_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='abstract',
            field=models.CharField(max_length=900, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='video',
            name='abstract',
            field=models.CharField(max_length=900, verbose_name='简介'),
        ),
    ]