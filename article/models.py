from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    Title = models.CharField(max_length=200)
    Summary = models.CharField(max_length=200)
    Body = models.TextField()
    Photo = models.ImageField(upload_to='images/', blank=True)
    Date = models.DateTimeField(auto_now_add = True)
    Author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])