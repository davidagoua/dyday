from django.urls import path
from.views import *

app_name = 'compte'
urlpatterns = [
    path('<slug>/profile', ProfileView.as_view(), name='profile'),
    path('<slug>/profile/update', ProfileView.update_profile, name='profile_update'),
    path('<int:pk>/suivre', suivre, name='suivre'),
    path('<int:pk>/forget', abandonner, name='forget'),
    path('profile-suggestions', ProfileListView.as_view(), name='profile_list'),
    path('notifcations', NoteListView.as_view(), name='note_list'),
]