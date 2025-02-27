import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Account, Department, Invoice

class InvoiceTable(NetBoxTable):
    invoice_id = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Invoice
        fields = ('pk', 'id', 'invoice_id', 'approval_date', 'department', 'account', 'amount', 'currency', 'comments', 'defined_period', 'period', 'actions')
        default_columns = ('invoice_id', 'department', 'account', 'amount', 'currency')

class DepartmentTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    invoice_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Department
        fields = ('pk', 'id', 'name', 'dep_id', 'invoice_count', 'actions')
        default_columns = ('name', 'dep_id', 'invoice_count')

class AccountTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    invoice_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Account
        fields = ('pk', 'id', 'name', 'number', 'invoice_count', 'comments', 'actions')
        default_columns = ('name', 'number', 'invoice_count')
