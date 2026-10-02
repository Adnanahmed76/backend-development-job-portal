from django.db import models

# invoice

class Invoice(models.Model):
    customer_name=models.CharField(max_length=300)
    invoice_number=models.CharField(max_length=50)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date_created=models.DateField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    notes=models.TextField(blank=True)
    name=models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.invoice_number



