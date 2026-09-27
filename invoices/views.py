from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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