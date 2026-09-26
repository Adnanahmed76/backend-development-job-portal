from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def show_invoice(request):
    return HttpResponse("your invoice page")


def show_invoices(request):
    data = {
        'customer_name': 'Rahul',
        'invoice_total': 1000
    }
    return JsonResponse(data)

def homepage(request):
    data={
        'my_name':"adnan",
        'my_age':25
    }
    return render(request,'home.html')