"""
For creating objects in the UI
"""
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm
from utilities.forms import CSVModelForm
from utilities.forms.rendering import FieldSet
from utilities.forms.fields import CommentField, DynamicModelChoiceField, CSVModelChoiceField
from ipam.models import Prefix
from extras.models import tags
from .models import Account, Department, Invoice, CurrencyChoices

from django import forms

class InvoiceForm(NetBoxModelForm):
    comments = CommentField()
    account = DynamicModelChoiceField(
        queryset=Account.objects.all()
    )
    department = DynamicModelChoiceField(
        queryset=Department.objects.all()
    )

    class Meta:
        model = Invoice
        fields = ('invoice_id', 'currency', 'amount', 'account', 'department', 'approval_date', 'defined_period', 'period', 'comments', 'tags')

class InvoiceBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Invoice.objects.all(),
        widget=forms.MultipleHiddenInput()
    )

    currency = forms.ChoiceField(
        required=False,
        choices=CurrencyChoices.CHOICES
    )
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        required=False
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False
    )

    model = Invoice
    fieldsets = (
        FieldSet('currency', 'account', 'department'),
    )

class InvoiceCSVForm(CSVModelForm):
    department = CSVModelChoiceField(
        queryset=Department.objects.all(),
        to_field_name='dep_id',
    )
    account = CSVModelChoiceField(
        queryset=Account.objects.all(),
        to_field_name='number'
    )
    currency = forms.ChoiceField(
        choices=CurrencyChoices.CHOICES,
        required=False,
        initial='nok'
    )
    class Meta:
        model = Invoice
        fields = [
            'invoice_id', 'department', 'account', 'amount', 'currency', 'amount', 'approval_date', 'comments', 'defined_period', 'period'
        ]
    def clean_currency(self):
        data = self.cleaned_data.get('currency')
        if not data:
            return 'nok'
        return data

class InvoiceFilterForm(NetBoxModelFilterSetForm):
    model = Invoice
    account = forms.ModelMultipleChoiceField(
        queryset=Account.objects.all(),
        required=False
    )
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        required=False
    )
    index = forms.IntegerField(
        required=False
    )


class AccountForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Account
        fields = ('name', 'number', 'comments', 'tags')

class AccountCSVForm(CSVModelForm):
    class Meta:
        model = Account
        fields = ['name', 'number', 'comments']

class DepartmentForm(NetBoxModelForm):
    
    class Meta:
        model = Department
        fields = ('name', 'dep_id', 'tags')

class DepartmentCSVForm(CSVModelForm):
    class Meta:
        model = Department
        fields = ['name', 'dep_id']
