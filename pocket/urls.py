from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pocket.core.urls', namespace='core')),
    path('accounts/', include('pocket.accounts.urls')),  # without namespace
    path('crm/', include('pocket.crm.urls', namespace='crm')),
    path('financial/', include('pocket.financial.urls', namespace='financial')),
    path('admin/', admin.site.urls),
]
