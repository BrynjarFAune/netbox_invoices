from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_invoices'

router = NetBoxRouter()
router.register('accounts', views.AccountViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('invoices', views.InvoiceViewSet)

urlpatterns = router.urls
