from django.db import models
from django.utils import timezone
from user.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    dateCreation = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-dateCreation']  # Most recent posts first
    
    def __str__(self):
        return f"{self.title} by {self.user.email}"
    
    @property
    def likes_count(self):
        return self.likes.count()




class Like():
    dateLike = models.DateField(default=timezone.now)
    userID = models.IntegerField()