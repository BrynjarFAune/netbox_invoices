from netbox.plugins import PluginConfig

class NetBoxInvoices(PluginConfig):
    name = 'netbox_invoices'
    verbose_name = ' NetBox Invoices'
    description = 'Manage invoices in NetBox'
    version = '0.1'
    base_url = 'invoices'

config = NetBoxInvoices
