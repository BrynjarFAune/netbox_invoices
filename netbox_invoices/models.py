from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from netbox.models.features import ImageAttachmentsMixin
from utilities.choices import ChoiceSet
from django.urls import reverse


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
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('number', 'name')
    def __str__(self):
        return f'{self.number} - {self.name}'
    def get_absolute_url(self):
        return reverse('plugins:netbox_invoices:account', args=[self.pk])

class Department(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    dep_id = models.PositiveIntegerField()
    def get_absolute_url(self):
        return reverse('plugins:netbox_invoices:department', args=[self.pk])
    def __str__(self):
        return f'{self.dep_id} - {self.name}'

class Invoice(NetBoxModel, ImageAttachmentsMixin):
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
        choices=CurrencyChoices,
        default='nok'
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.PROTECT,
        related_name='invoices'
    )
    defined_period = models.PositiveIntegerField()
    period = models.PositiveIntegerField()
    class Meta:
        ordering = ('approval_date', 'invoice_id')
    def __str__(self):
        return f'{self.account}'
    def get_absolute_url(self):
        return reverse('plugins:netbox_invoices:invoice', args=[self.pk])
