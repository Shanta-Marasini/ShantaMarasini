from django.urls import path
from .views import Project

urlpatterns = [
    path('github/', Project.as_view(), name='github'),
]