# Generated by Django 3.0.4 on 2021-06-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='markdown',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='125555'),
            preserve_default=False,
        ),
    ]
