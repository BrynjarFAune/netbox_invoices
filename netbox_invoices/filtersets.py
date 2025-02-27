from netbox.filtersets import NetBoxModelFilterSet
from .models import Invoice, Account, Department

class InvoiceFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Invoice
        fields = ('id', 'invoice_id', 'account', 'department')
