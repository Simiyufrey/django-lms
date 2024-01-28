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
from django.conf import settings
import base64
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
        # cl = MpesaClient()
        form=request.POST
        phone_number = form['phone']
        amount = int(form['amount'])
        account_reference = 'Godfrey Wayne'
        transaction_desc = 'CustomerBaybillOnline'
        callback_url = 'https://28f9-41-90-182-96.ngrok-free.app/payment/success'
        
        access_token=accessToken()
        response = stk_push(phone_number, amount,access_token)
        print(response)
        print(response)
        return HttpResponse({"success":True,"resposnse":response})
    else: 
       
        return render(request,"lipa/payment.html")
    
def generateTimestamp():
    timestamp=datetime.strftime(datetime.now(),"%Y%m%d%H%M%S")
    return timestamp


def accessToken():
    auth=base64.b64encode(str(settings.CONSUMER_KEY+":"+settings.CONSUMER_SECRET).encode())
    headers={
        "Authorization":"Basic "+auth.decode(),
        "Content-Type":"application/json; charset=utf-8"
    }

    req=requests.get(settings.ACCESS_URL,headers=headers)
    
    return req.json()['access_token']


def stk_push(amount,phone,token):
        print(settings.MPESA_SHORTCODE)

        payload= {
    
            "Password": base64.b64encode(str(settings.MPESA_SHORTCODE+settings.MPESA_PASSKEY+generateTimestamp()).encode()).decode(),
            "Timestamp": generateTimestamp(),
            "BusinessShortCode":settings.MPESA_SHORTCODE,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": "https://0ca0-154-122-7-250.ngrok-free.app/payment/success",
            "AccountReference": "GMD HOTEL",
            "TransactionDesc": "Taxayo"
        }

        print(payload['BusinessShortCode']," received")
        headers={
            "Authorization":f"Bearer {token}"
        }

        req=requests.post(settings.STK_URL,headers=headers,data=json.dumps(payload))
        return req.json()

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
