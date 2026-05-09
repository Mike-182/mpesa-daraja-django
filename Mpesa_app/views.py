from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


def stk_push_success(request):
    if request.method == 'POST':
        # 1. Get the data from the form
        phone_number = request.POST.get('phone')
        amount = int(request.POST.get('amount'))

        # 2. Initialize the M-Pesa Client
        client = MpesaClient()
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'

        # 3. Send the STK Push with the dynamic values
        response = client.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        return HttpResponse(f"STK Push sent to {phone_number} for KES {amount}. Check your phone!")

    # If the request is GET (loading the page), just show the form
    return render(request, 'index.html')