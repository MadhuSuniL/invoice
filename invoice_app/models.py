from django.db import models

# Create your models here.

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.IntegerField()
    customer_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.customer_name +' '+ str(self.invoice_no)
    
    
    
class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    price = models.FloatField()

    
    def __str__(self):
        return self.invoice.customer_name
    
    