from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('poster', post, name='poster'),
    path('liker/<int:pk>', liker, name='liker'),
]

