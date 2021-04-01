from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from PIL import Image
# Create your models here.
 
class profile(models.Model):
    user=OneToOneField(User,on_delete=CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self) -> str:
        return f"{self.user.username} profile"

    
    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            img.thumbnail((300,300))
            img.save(self.image.path) 