from rest_framework import serializers
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer

class CommentSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializerAPI(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
