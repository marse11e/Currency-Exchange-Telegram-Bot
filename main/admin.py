from django.contrib import admin
from .models import TelegramUser, TelegramAds


@admin.register(TelegramAds)
class TelegramAdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'text', 'url', 'url2', 'created_at']
    search_fields = ['text', 'url', 'url2']
    readonly_fields = ['created_at']


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ["user_id", "username", "first_name", "last_name", "admin", "created_at"]
    list_filter = ["admin", "created_at"]
    search_fields = ["user_id", "username", "first_name", "last_name"]
    ordering = ["-created_at"]
