# Generated by Django 3.0.4 on 2020-03-25 11:13

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
            name='userPro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='userPro/avatar')),
                ('hito', models.CharField(default='Nothing to say.', max_length=40, verbose_name='个性签名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
