from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    experience = models.PositiveIntegerField(default=0, help_text='Years of experience')

    def __str__(self):
        return f"{self.user.username}'s profile"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
