from PIL import Image

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self) -> str:
        return f"{self.user.username} Profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            reduced_size = (300, 300)
            img.thumbnail(reduced_size)
            img.save(self.image.path)
