from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from partners.models import Partner


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='products_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='products_updated'
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('outcome', 'Outcome')
    )

    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='sales'
    )
    client = models.ForeignKey(
        Partner,
        on_delete=models.SET_NULL,
        null=True,
        related_name='purchases'
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name}"


@receiver(pre_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    if not instance.pk:
        qty = instance.quantity
        if instance.transaction_type == 'outcome':
            qty *= -1
    else:
        previous_transaction = Transaction.objects.get(pk=instance.pk)
        previous_qty = previous_transaction.quantity
        current_qty = instance.quantity
        qty = current_qty - previous_qty
        if instance.transaction_type == 'outcome':
            qty *= -1

    instance.product.stock += qty
    instance.product.save()