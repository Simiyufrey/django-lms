from django.db import models

# Create your models here.


class Transaction(models.Model):
    transaction_code=models.CharField(primary_key=True,max_length=20)
    merchant_id=models.CharField(max_length=30)
    Phone_number=models.CharField(max_length=15)
    Checkout_id=models.CharField(max_length=20)
    Amount=models.CharField(max_length=30)
    date_transacted=models.DateTimeField()
    completed=models.CharField(max_length=20,default="Pending")
    
    
    
    

    