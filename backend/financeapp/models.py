from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    class Type(models.TextChoices):
        CHECKING = "checking"
        SAVINGS = "savings"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=Type.choices)
    currency = models.CharField(max_length=3, default="NOK")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Category(models.Model):
    class Kind(models.TextChoices):
        INCOME = "income"
        EXPENSE = "expense"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=10, choices=Kind.choices)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)


class Transaction(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2
    )  # negative = money out
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        indexes = [models.Index(fields=["account", "date"])]


class RecurringTransaction(models.Model):
    class IntervalTypes(models.TextChoices):
        DAILY = "daily"
        WEEKLY = "weekly"
        MONTHLY = "monthly"
        YEARLY = "yearly"

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="recurring_transactions"
    )
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    amount = models.DecimalField(
        max_digits=12, decimal_places=2
    )  # negative = money out
    interval = models.CharField(max_length=20, choices=IntervalTypes.choices)
    next_date = models.DateField(default=timezone.localdate)
