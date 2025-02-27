from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Account, Department, Invoice
from ipam.api.serializers import PrefixSerializer

class AccountSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_invoices-api:account-detail'
    )
    invoice_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Account
        fields = (
            'id', 'url', 'display', 'name', 'number', 'tags', 'custom_fields', 'created', 'last_updated', 'invoice_count'
        )

class DepartmentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_invoices-api:department-detail'
    )
    invoice_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Department
        fields = (
            'id', 'url', 'display', 'name', 'dep_id', 'tags', 'custom_fields', 'created', 'last_updated', 'invoice_count'
        )

class NestedAccountSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins_api:netbox_invoices-api:account-detail'
    )

    class Meta:
        model = Account
        fields = ('id', 'url', 'display', 'name', 'number')
    
class NestedDepartmentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins_api:netbox_invoices-api:department-detail'
    )
    
    class Meta:
        model = Department
        fields = ('id', 'url', 'display', 'name', 'dep_id')

class InvoiceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_invoices-api:invoice-detail'
    )
    account = AccountSerializer()
    department = DepartmentSerializer()
    # source_prefix = PrefixSerializer()
    # destination_prefix = PrefixSerializer()

    class Meta:
        model = Invoice
        fields = (
            'id', 'url', 'display', 'invoice_id', 'amount', 'currency', 'department', 'account', 'comments', 'description', 'approval_date', 'defined_period', 'period', 'tags', 'custom_fields', 'created', 'last_updated'
        )
