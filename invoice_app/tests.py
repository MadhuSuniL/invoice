from django.test import TestCase
from rest_framework.test import APITestCase
import datetime


class InvoiceAPITestCase(APITestCase):
    
    def test_for_post_api(self):
        url = '/post_invoice'
        data = {
            'invoice_no': 100,
            'date': datetime.datetime.now().date(),
            'customer_name': 'Madhu',
            'description' : 'DEs',
            'quantity' : 10,
            'unit_price' : 100.5,
            'price' : 100.9
            }
        
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'msg':'Object Created!'})

    
    def test_for_get_api(self):
        url = '/get_invoice/'
        
        response = self.client.get(url,follow=True)
        self.assertEqual(response.status_code, 200)

