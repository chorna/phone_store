from django.contrib import admin

# Register your models here.

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ruc', 'city', 'address')
    list_filter = ('is_client', 'is_supplier')
    search_fields = ('name', 'ruc', 'last_name')