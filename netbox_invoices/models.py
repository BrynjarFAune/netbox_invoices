from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class CurrencyChoices(ChoiceSet):
    key = 'Invoice.currency'

    CHOICES = [
        ('nok', 'NOK'),
        ('dkk', 'DKK'),
        ('eur', 'EUR'),
        ('usd', 'USD'),
    ]

class Account(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    number = models.PositiveIntegerField()
    description = models.CharField(
        max_length=30
    )
    class Meta:
        ordering = ('number', 'name')
    def __str__(self):
        return self.name

class Invoice(NetBoxModel):
    invoice_id = models.PositiveIntegerField()
    comments = models.TextField(
        blank=True
    )
    description = models.CharField(
        max_length=30
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    approval_date = models.DateField()
    account = models.ForeignKey(
        to=Account,
        on_delete=models.PROTECT,
        related_name='invoices'
    )
    currency = models.CharField(
        max_length=10,
        choices=CurrencyChoices
    )
    class Meta:
        ordering = ('approval_date', 'invoice_id')
    def __str__(self):
        return f'{self.account}'
