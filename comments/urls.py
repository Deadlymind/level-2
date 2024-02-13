# Inside comments/urls.py
from django.urls import path
from .views import post_detail, add_comments

urlpatterns = [
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_comments/<int:post_id>/', add_comments, name='add_comment'),  # Add 'name' parameter
]
