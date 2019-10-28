from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('r/<slug:subreddit>/', views.index, name='subreddit'),
]