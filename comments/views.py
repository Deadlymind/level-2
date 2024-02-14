from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Post, Comment
from .forms import CommentForm
from .serializers import PostSerializer

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'comments/post_detail.html', {'post': post, 'comments': comments})

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'comments/post_detail.html', {'form': form, 'post': post})

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
