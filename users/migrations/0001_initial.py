# Generated by Django 3.0.4 on 2021-06-04 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPro',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pro', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(default='User One', max_length=16, verbose_name='昵称')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='%Y/userPro/avatar')),
                ('motoo', models.CharField(default='Nothing to say.', max_length=40, verbose_name='个性签名')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
