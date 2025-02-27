## netbox-invoices

Manage invoices in NetBox

Models:
- Account: bank account with name and number
- Department: department with name and number
- Invoice: Invoices with currency options, ++, tied to related account and department. includes image attachment

Currency choices, along with all models, are located in "netbox_invoices/models.py" if you want to add / remove options.

Faults:
- No Bulk Edit
- No connection to devices
