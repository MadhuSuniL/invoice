from django.contrib import admin
from django.urls import path , include
from invoice_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('invoice/',include('invoice_app.urls'))
]
