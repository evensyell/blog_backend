# Generated by Django 3.0.4 on 2020-08-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200819_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='article',
            name='share',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
