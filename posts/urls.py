from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    CommentListCreateAPIView,
)

urlpatterns = [
    path("", PostListCreateAPIView.as_view()),
    path("<int:pk>/", PostDetailAPIView.as_view()),
    path("<int:id>/comments/", CommentListCreateAPIView.as_view()),
]
