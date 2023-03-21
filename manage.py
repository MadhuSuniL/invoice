#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoice.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()









# $('.create').click(function(){

#     invoice_no = document.getElementById('no').value
#     customer_name = document.getElementById('name').value
#     date = document.getElementById('date').value
#     description = document.getElementById('des').value
#     quantity = document.getElementById('q').value
#     unit_price = document.getElementById('up').value
#     price = document.getElementById('p').value


#     $.ajax({
#         url:'/invoice/post_invoice',
#         method:'post',
#         data:{
#             invoice_no,
#             customer_name,
#             date,
#             description,
#             quantity,
#             unit_price,
#             price
#         },
#         success:function(){
#             window.location.reload()
#         },
#         error:function(){
#             alert('err')
#         }
#     })


# })

# <div class="fixed shadow-lg border-2 w-[92%] md:w-[30%] bg-gray-300 border-black rounded-lg p-3 md:m-2 left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%]">
#         <center>
#                 <h1 class="text-xl font-bold">Create Invoice</h1><br>
#             <input type="number" class="p-2 w-full" id="no" placeholder="Invoice No"><br><br>
#             <input type="text"  class="p-2 w-full" id="name" placeholder="Customer Name"><br><br>
#             <input type="date" class="p-2 w-full" id="date"><br><br>
#             <input type="text" class="p-2 w-full" id="des"><br><br>
#             <input type="number" class="p-2 w-full" id="q"><br><br>
#             <input type="number" class="p-2 w-full" id="up"><br><br>
#             <input type="number" class="p-2 w-full" id="p"><br><br>
#         </center>
#     <button class="create bg-green-500 p-2 rounded-lg float-right text-white border-2 border-black animate-pulse hover:scale-110 m-3">Create</button><br>
    