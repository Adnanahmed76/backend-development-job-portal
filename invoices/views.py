from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Invoice

#create a new record
def create_invoice(request):
    Invoice.objects.create(
        customer_name='Abdul Razzak',
        invoice_number='INC-200',
        amount=15000.00,
        is_paid=False
    )

    return render(request,'bill.html',{})
#fetch record
def show_one_invoice(request):
    invoice=Invoice.objects.get(invoice_number='INC-200')
    data={
        'invoice':invoice
    }
    return render(request,'details.html',data)

def show_invoice(request):
    return HttpResponse("your invoice page")


def show_invoices(request):
    data = {
        'all_invoices':[
{"number":1,'customer':'Adnan','amount':9000},
{"number":1,'customer':'Adnan','amount':5000},
{"number":1,'customer':'Adnan','amount':5000}


        ]
        
    }
    return render(request,'bill.html',data)

def homepage(request):
    data={
        'my_name':"adnan",
        'my_age':25
    }
    return render(request,'home.html')