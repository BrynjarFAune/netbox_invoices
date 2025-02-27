"""
Processing requests, usually has an assocuated URL and handles HTTP types like POST, GET, ...
"""
from netbox.views import generic
from . import filtersets, forms, models, tables
from django.db.models import Count

# Account views
class AccountView(generic.ObjectView):
    queryset = models.Account.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.InvoiceTable(instance.invoices.all())
        table.configure(request)

        return {
            'invoice_table': table
        }

class AccountListView(generic.ObjectListView):
    queryset = models.Account.objects.annotate(
        invoice_count=Count('invoices')
    )
    table = tables.AccountTable

class AccountEditView(generic.ObjectEditView):
    queryset = models.Account.objects.all()
    form = forms.AccountForm

class AccountDeleteView(generic.ObjectDeleteView):
    queryset = models.Account.objects.all()

class AccountBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Account.objects.all()
    table = tables.AccountTable
    default_return_url = 'plugins:netbox_invoices:account_list'

class AccountBulkImportView(generic.BulkImportView):
    queryset = models.Account.objects.all()
    model_form = forms.AccountCSVForm
    table = tables.AccountTable

# Department views
class DepartmentView(generic.ObjectView):
    queryset = models.Department.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.InvoiceTable(instance.invoices.all())
        table.configure(request)

        return {
            'invoice_table': table
        }

class DepartmentListView(generic.ObjectListView):
    queryset = models.Department.objects.annotate(
        invoice_count=Count('invoices')
    )
    table = tables.DepartmentTable

class DepartmentEditView(generic.ObjectEditView):
    queryset = models.Department.objects.all()
    form = forms.DepartmentForm

class DepartmentDeleteView(generic.ObjectDeleteView):
    queryset = models.Department.objects.all()

class DepartmentBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Department.objects.all()
    table = tables.DepartmentTable
    default_return_url = 'plugins:netbox_invoices:department_list'

class DepartmentBulkImportView(generic.BulkImportView):
    queryset = models.Department.objects.all()
    model_form = forms.DepartmentCSVForm
    table = tables.DepartmentTable

# Invoice views
class InvoiceView(generic.ObjectView):
    queryset = models.Invoice.objects.all()

class InvoiceListView(generic.ObjectListView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable
    filterset = filtersets.InvoiceFilterSet
    filterset_form = forms.InvoiceFilterForm

class InvoiceEditView(generic.ObjectEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceForm

class InvoiceDeleteView(generic.ObjectDeleteView):
    queryset = models.Invoice.objects.all()

class InvoiceBulkImportView(generic.BulkImportView):
    queryset = models.Invoice.objects.all()
    model_form = forms.InvoiceCSVForm
    table = tables.InvoiceTable

class InvoiceBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Invoice.objects.all()
    table = tables.InvoiceTable
    default_return_url = 'plugins:netbox_invoices:invoice_list'

class InvoiceBulkEditView(generic.BulkEditView):
    queryset = models.Invoice.objects.all()
    form = forms.InvoiceBulkEditForm
    table = tables.InvoiceTable
    default_return_url = 'plugins:netbox_invoices:invoice_list'
