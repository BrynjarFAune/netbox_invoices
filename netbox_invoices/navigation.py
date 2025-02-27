from netbox.plugins import PluginMenuItem, PluginMenuButton
from netbox.choices import ButtonColorChoices

account_buttons = [
    PluginMenuButton(
        link='plugins:netbox_invoices:account_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
    PluginMenuButton(
        link='plugins:netbox_invoices:account_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]
department_buttons = [
    PluginMenuButton(
        link='plugins:netbox_invoices:department_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
    PluginMenuButton(
        link='plugins:netbox_invoices:department_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]
invoice_buttons = [
    PluginMenuButton(
        link='plugins:netbox_invoices:invoice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
    ),
    PluginMenuButton(
        link='plugins:netbox_invoices:invoice_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_invoices:invoice_list',
        link_text='Invoices',
        buttons=invoice_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_invoices:account_list',
        link_text='Accounts',
        buttons=account_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_invoices:department_list',
        link_text='Departments',
        buttons=department_buttons
    )
)

