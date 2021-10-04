from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('blogs/', PostList.as_view(), name='posts'),
    path('blog/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]



