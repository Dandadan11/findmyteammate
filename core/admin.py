from django.contrib import admin
from .models import Game, Profile

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'game', 'rank', 'created_at']
    list_filter = ['game', 'rank']
    search_fields = ['title', 'user__username']