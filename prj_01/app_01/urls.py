from django.urls import path
from .views import PostList, PostUpdate, PostCreate, ResponseList, ResponseCreate


urlpatterns = [
    path('post/', PostList.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
    path('post/response/', ResponseList.as_view(), name='response'),
    path('post/response/create/', ResponseCreate.as_view(), name='response_create'),
]
