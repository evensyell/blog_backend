# Generated by Django 3.2.4 on 2021-06-17 15:01

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210607_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='img/article_img/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='markdown',
            field=models.FileField(blank=True, upload_to='markdown/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.FileField(upload_to='music/'),
        ),
    ]
