from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import AccountSerializer, DepartmentSerializer, InvoiceSerializer

class InvoiceViewSet(NetBoxModelViewSet):
    queryset = models.Invoice.objects.prefetch_related(
        'account', 'department', 'source_prefix', 'destination_prefix', 'tags'
    )
    serializer_class = InvoiceSerializer

class DepartmentViewSet(NetBoxModelViewSet):
    queryset = models.Department.objects.prefetch_related('tags').annotate(
        invoice_count=Count('invoices')
    )
    serializer_class = DepartmentSerializer

class AccountViewSet(NetBoxModelViewSet):
    queryset = models.Account.objects.prefetch_related('tags').annotate(
        invoice_count=Count('invoices')
    )
    serializer_class = AccountSerializer
