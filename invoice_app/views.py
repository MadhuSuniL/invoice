from django.shortcuts import render
from rest_framework.generics import ListAPIView , CreateAPIView
from .models import *
from .serializers import InvoiceSerializer ,InvoiceDetailSerializer
# Create your views here.



class InvoicePOSTAPIView(CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceGETAPIView(ListAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailSerializer
    
    
def index(request):
    
    objs = Invoice.objects.all().values()
    objs2 = InvoiceDetails.objects.all().values()
    list_data = []
    for o1,o2 in zip(objs,objs2):
        data = {}
        for i in dict(o1):
            data[i] = o1[i]
        for i in dict(o2):
            data[i] = o2[i]
        list_data.append(data)
    
    print(list_data)
    
    data = {'data':list_data}    
    return render(request, 'index.html',data)