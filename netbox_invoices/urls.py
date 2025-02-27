from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    # Invoices
    path('invoices/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/add/', views.InvoiceEditView.as_view(), name='invoice_add'),
    path('invoices/<int:pk>/', views.InvoiceView.as_view(), name='invoice'),
    path('invoices/<int:pk>/edit/', views.InvoiceEditView.as_view(), name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice_delete'),
    path('invoices/bulk-delete', views.InvoiceBulkDeleteView.as_view(), name='invoice_bulk_delete'),
    path('invoices/import/', views.InvoiceBulkImportView.as_view(), name='invoice_import'),
    #path('invoices/bulk-edit', views.InvoiceBulkEditView.as_view(), name='invoice_bulk_edit'),
    path('invoices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='invoice_changelog', kwargs={
        'model': models.Invoice
    }),

    # Accounts
    path('accounts/', views.AccountListView.as_view(), name='account_list'),
    path('accounts/add/', views.AccountEditView.as_view(), name='account_add'),
    path('accounts/<int:pk>/', views.AccountView.as_view(), name='account'),
    path('accounts/<int:pk>/edit/', views.AccountEditView.as_view(), name='account_edit'),
    path('accounts/<int:pk>/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
    path('accounts/bulk-delete', views.AccountBulkDeleteView.as_view(), name='account_bulk_delete'),
    path('accounts/import/', views.AccountBulkImportView.as_view(), name='account_import'),
    path('accounts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='account_changelog', kwargs={
        'model': models.Account
    }),

    # Departments
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/add/', views.DepartmentEditView.as_view(), name='department_add'),
    path('departments/<int:pk>/', views.DepartmentView.as_view(), name='department'),
    path('departments/<int:pk>/edit/', views.DepartmentEditView.as_view(), name='department_edit'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('departments/bulk-delete', views.DepartmentBulkDeleteView.as_view(), name='department_bulk_delete'),
    path('departments/import/', views.DepartmentBulkImportView.as_view(), name='department_import'),
    path('departments/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='department_changelog', kwargs={
        'model': models.Department
    }),
)
