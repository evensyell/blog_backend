from django.db import models
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import User


class UserPro(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="pro"
    )
    avatar = ProcessedImageField(upload_to="userPro/avatar", blank=True)
    hito = models.CharField("个性签名", max_length=40, default="Nothing to say.")

