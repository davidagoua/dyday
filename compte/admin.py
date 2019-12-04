from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk','user','slug','points']


@admin.register(Notification)
class NotifcationAdmin(admin.ModelAdmin):
    list_display = ['link']

@admin.register(NotificationBox)
class NotificationBoxAdmin(admin.ModelAdmin):
    list_display = ['user']