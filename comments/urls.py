from django.urls import path
from .views import post_detail, add_comment, PostDetailAPIView

urlpatterns = [
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail_api'),
]
