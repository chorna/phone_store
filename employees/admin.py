from django.contrib import admin

# Register your models here.

from .models import Employees


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'date_joined', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name')
