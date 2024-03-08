from django.contrib import admin
from prize.models import Prize


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    """
    Админка для вознагражения
    """
    list_display = ('title', 'user',)
    list_filter = ('user',)
