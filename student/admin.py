from django.contrib import admin
from .models import Student, University

admin.site.register(University)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'total_contract', 'received_amount', 'university')
    list_filter = ('university', 'created_at', 'total_contract', 'received_amount')
    search_fields = ('name', 'university')
    ordering = ('-created_at',)
