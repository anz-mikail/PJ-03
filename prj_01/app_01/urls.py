from django.urls import path
from .views import PostList, PostUpdate, PostCreate, ResponseList, ResponseCreate, ResponseDelete


urlpatterns = [
    path('post/', PostList.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
    path('response/', ResponseList.as_view(), name='response'),
    path('response/create/', ResponseCreate.as_view(), name='response_create'),
    path('response/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete')
]
