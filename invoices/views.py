from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_invoice(request):
    return HttpResponse("your invoce page")