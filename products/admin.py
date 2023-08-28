from django.contrib import admin

from .models import Product, Transaction


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('seller', 'client', 'transaction_type', 'quantity', 'product',
                    'timestamp')
    list_filter = ('transaction_type',)
    search_fields = ('seller__username', 'client__username', 'product__name')
