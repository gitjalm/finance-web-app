from rest_framework import serializers
from .models import Account, Category, Transaction, RecurringTransaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "user", "name", "type", "currency", "balance"]
        read_only_fields = ["user"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "user", "name", "kind", "parent"]
        read_only_fields = ["user"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "account",
            "category",
            "amount",
            "date",
            "description",
            "created_at",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request:
            self.fields["account"].queryset = Account.objects.filter(user=request.user)
            self.fields["category"].queryset = Category.objects.filter(
                user=request.user
            )


class RecurringTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = [
            "id",
            "account",
            "category",
            "amount",
            "interval",
            "next_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request:
            self.fields["account"].queryset = Account.objects.filter(user=request.user)
            self.fields["category"].queryset = Category.objects.filter(
                user=request.user
            )
