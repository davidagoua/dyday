from django.contrib import admin
from .models import *


@admin.register(SimplePost)
class SimplePostAdmin(admin.ModelAdmin):

    list_display = ['user','time','likes']