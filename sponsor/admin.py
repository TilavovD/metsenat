from django.contrib import admin
from .models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'total_amount', 'spent_amount', 'status')
    list_filter = ('status', 'created_at', 'total_amount', 'spent_amount')
    search_fields = ('name', 'company')
    ordering = ('status', '-created_at')
