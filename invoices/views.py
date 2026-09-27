import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Invoice


def homepage(request):

    all_invoices = Invoice.objects.all()

    data = {
        'all_invoices': all_invoices,
        'total_invoices': Invoice.objects.count(),
        'paid_invoices': Invoice.objects.filter(is_paid=True).count(),
        'unpaid_invoices': Invoice.objects.filter(is_paid=False).count(),
    }

    return render(request, 'home.html', data)


def show_invoices(request):

    all_invoices = Invoice.objects.all()

    data = {
        'all_invoices': all_invoices,
    }

    return render(request, 'details.html', data)


def show_unpaid_invoices(request):

    unpaid_invoices = Invoice.objects.filter(is_paid=False)

    data = {
        'unpaid_invoices': unpaid_invoices,
    }

    return render(request, 'unpaid_invoices.html', data)


def show_invoice(request):

    all_invoices = Invoice.objects.all()

    data = {
        'all_invoices': all_invoices,
    }

    return render(request, 'bill.html', data)


@csrf_exempt
def create_invoice(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        customer_name = data.get('customer_name')
        invoice_number = data.get('invoice_number')
        amount = data.get('amount')
        is_paid = data.get('is_paid', False)
        notes = data.get('notes', '')

        invoice = Invoice.objects.create(
            customer_name=customer_name,
            invoice_number=invoice_number,
            amount=amount,
            is_paid=is_paid,
            notes=notes
        )

        return JsonResponse({
            'message': 'Invoice created successfully',
            'id': invoice.id,
            'invoice_number': invoice.invoice_number
        })

    return JsonResponse({
        'message': 'Only POST request is allowed'
    })


def invoice_detail(request, invoice_id):

    try:
        invoice = Invoice.objects.get(id=invoice_id)

        return JsonResponse({
            'id': invoice.id,
            'customer_name': invoice.customer_name,
            'invoice_number': invoice.invoice_number,
            'amount': str(invoice.amount),
            'date_created': str(invoice.date_created),
            'is_paid': invoice.is_paid,
            'notes': invoice.notes
        })

    except Invoice.DoesNotExist:

        return JsonResponse({
            'message': 'Invoice not found'
        }, status=404)