from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'comments/post_detail.html', {'post': post, 'comments': comments})

def add_comments(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'comments/add_comments.html', {'form': form, 'post': post})
