from django.urls import path
from .views import *

urlpatterns = [
    path('get_invoice/', InvoiceGETAPIView.as_view()),
    path('post_invoice', InvoicePOSTAPIView.as_view()),
]
