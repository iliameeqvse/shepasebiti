from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    skills = serializers.CharField(source='profile.skills', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'skills']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'bio', 'skills', 'experience']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
