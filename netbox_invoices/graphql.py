from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models

class InvoiceType(NetBoxObjectType):

    class Meta:
        model = models.Invoice
        fields = '__all__'

class DepartmentType(NetBoxObjectType):

    class Meta:
        model = models.Department
        fields = '__all__'

class AccountType(NetBoxObjectType):

    class Meta:
        model = models.Department
        fields = '__all__'

class Query(ObjectType):
    invoice = ObjectField(InvoiceType)
    invoice_list = ObjectField(InvoiceType)

    department = ObjectField(DepartmentType)
    department_list = ObjectField(DepartmentType)

    account = ObjectField(AccountType)
    account_list = ObjectField(AccountType)

schema = Query
