from netbox.search import SearchIndex, register_search
from .models import Account, Invoice, Department

@register_search
class InvoiceIndex(SearchIndex):
    model = Invoice
    fields = (
        ('invoice_id', 100),
        ('description', 5000)
    )
    display_attrs = ('invoice_id', 'currency', 'amount', 'description')

@register_search
class DepartmentIndex(SearchIndex):
    model = Department
    fields = (
        ('name', 200),
        ('dep_id', 100),
        ('comments', 5000)
    )
    display_attrs = ('dep_id', 'name', 'comments')

@register_search
class AccountIndex(SearchIndex):
    model = Account
    fields = (
        ('name', 200),
        ('number', 100),
        ('comments', 5000)
    )
    display_attrs = ('number', 'name', 'comments')

indexes = [
    AccountIndex,
    DepartmentIndex,
    InvoiceIndex,
]
