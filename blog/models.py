from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title=CharField(max_length=100)
    content=TextField()
    date_posted=DateField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})




