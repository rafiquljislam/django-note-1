from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):  # for redirect from create view
        return reverse('post_detail', kwargs={'pk' : self.pk})