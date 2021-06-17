from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User

# 引入内置信号
from django.db.models.signals import post_save

# 引入信号接收器的装饰器
from django.dispatch import receiver


class UserPro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pro",primary_key=True)
    nickname = models.CharField("昵称", max_length=16, default="User One")
    avatar = ProcessedImageField(upload_to="img/avatar", blank=True)
    motoo = models.CharField("个性签名", max_length=40, default="Nothing to say.")

    class Meta:
        ordering = ("pk",)

 
# 信号接收函数，每当新建 User 实例时自动调用
@receiver(post_save, sender=User)
def create_user_pro(sender, instance, created, **kwargs):
    if created:
        UserPro.objects.create(user=instance)


# 信号接收函数，每当更新 User 实例时自动调用
@receiver(post_save, sender=User)
def save_user_pro(sender, instance, **kwargs):
    instance.pro.save()
