from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from school_ms.settings import *
from django.views.decorators.csrf import requires_csrf_token
import json
from django.utils import timezone
from django.core import serializers
from . import models
# Create your views here.
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import ensure_csrf_cookie
from datetime import datetime, timedelta
from datetime import time
import requests

# @ensure_csrf_cookie
def success(request):
    if request.method == "POST":
        response=HttpResponse("cookier")
        expiry=datetime.now() + timedelta(days=7)
        response.set_cookie("my_cookie",expires=expiry,value=request.POST)
        save_data(body=request.body)
        return HttpResponse(request.POST)
    else:
       data= {'MerchantRequestID': '18752-10242463-1', 'CheckoutRequestID': 'ws_CO_12072023174108258746364856', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'RGC4D5JHOQ'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20230712174034}, {'Name': 'PhoneNumber', 'Value': 254746364856}]}}
       save_data(body=data)
       return HttpResponse("Saved")
@requires_csrf_token
def payment(request):
    if request.method =="POST":
        cl = MpesaClient()
        form=request.POST
        phone_number = form['phone']
        amount = int(form['amount'])
        account_reference = 'Godfrey Wayne'
        transaction_desc = 'CustomerBaybillOnline'
        callback_url = ' https://28f9-41-90-182-96.ngrok-free.app/payment/success'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        
        response=response.json()
        return HttpResponse({"success":True,"resposnse":response})
    else: 
       
        return render(request,"lipa/payment.html")
def getAccessToken():
    try:
        pass
        
    except Exception as e:
        pass

def save_data(body):
      
        try:
            
            data=json.loads(body)['Body']['stkCallback']
            
            if str(data['ResultDesc']).__contains__("successfully"):
                print("intiated")
                print(data)
                merchant_id=data['MerchantRequestID']
                checkout_id=data['CheckoutRequestID']
                metadata=data['CallbackMetadata']['Item']
                
                PhoneNumber=""
                transaction_code=""
                date_transacted=''
                
                Amount=""
                for meta in metadata:
                    column=meta['Name']
                    
                    if  column !="Balance":
                        if column =="Amount": 
                            value=meta['Value'] if meta['Value'] != None else ""
                            Amount=value
                        elif column =="MpesaReceiptNumber": 
                            value=meta['Value'] if meta['Value'] != None else ""
                            transaction_code=value
                        elif column =="PhoneNumber": 
                            value=meta['Value'] if meta['Value'] != None else ""
                            PhoneNumber=value
                        elif column =="TransactionDate": 
                            value=meta['Value'] if meta['Value'] != None else ""
                            date_transacted=datetime.strptime(str(value),"%Y%m%d%H%M%S")
                            django_date=timezone.make_aware(date_transacted,timezone=timezone.utc)
                            date_transacted=django_date.strftime("%Y-%m-%d %H:%M:%S")
                tans=models.Transaction(transaction_code=transaction_code,merchant_id=merchant_id,Phone_number=PhoneNumber,Checkout_id=checkout_id,Amount=Amount,date_transacted=date_transacted,completed="Completed")
                if tans.save():
                    print("Transaction saved successfully")
            else:
                print("Transaction cancelled")
        except Exception as e:
            print(e)
