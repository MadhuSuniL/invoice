from rest_framework.serializers import ModelSerializer , Serializer
from rest_framework import serializers
from .models import *


class InvoiceSerializer(Serializer):

    invoice_no = serializers.IntegerField(write_only=True)
    date = serializers.DateField(write_only=True)
    customer_name = serializers.CharField(write_only=True)
    description = serializers.CharField(write_only=True)
    quantity = serializers.IntegerField(write_only=True)
    unit_price = serializers.FloatField(write_only=True)
    price = serializers.FloatField(write_only=True)
    msg = serializers.CharField(read_only=True)
        
    def create(self, validated_data):
        # for first model
        invoice_no = validated_data.get('invoice_no')
        date = validated_data.get('date')
        customer_name = validated_data.get('customer_name')
        
        #for 2nd model
        description = validated_data.get('description')
        quantity = validated_data.get('quantity')
        unit_price = validated_data.get('unit_price')
        price = validated_data.get('price')
        
        invoice_obj = Invoice.objects.create(date=date,invoice_no = invoice_no,customer_name=customer_name)
        invoice_detail_obj = InvoiceDetails.objects.create(invoice=invoice_obj,description=description,quantity=quantity,unit_price=unit_price,price=price)        
        return {'msg':'Object Created!'}

class InvoiceSerializer2(ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'        


        
class InvoiceDetailSerializer(ModelSerializer):
    invoice = InvoiceSerializer2()
    class Meta:
        model = InvoiceDetails
        fields = '__all__'
        