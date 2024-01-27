import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
from datetime import date,datetime
from . import models

load_dotenv()
def getAccessToken(request):
    consumer_key="FTWn9sSpCGGfelG3uqqBH2UEAt6yND9L"
    consumer_secret="G7HBZj0vALmWZ6Ml"
    token_url=os.environ.get("TOKEN_URL")
    r=request.get(url=token_url,auth=HTTPBasicAuth(os.environ.get("CONSUMER_KEY"),os.environ.get("CONSUMER_SECRET")))
    
    token=json.loads(r.text)
    validate_token=token['access_token']
    return validate_token



body=b'{"Body":{"stkCallback":{"MerchantRequestID":"29601-14958601-1","CheckoutRequestID":"ws_CO_09072023182543738769702562","ResultCode":0,"ResultDesc":"The service request is processed successfully.","CallbackMetadata":{"Item":[{"Name":"Amount","Value":1.00},{"Name":"MpesaReceiptNumber","Value":"RG964PY5S0"},{"Name":"Balance"},{"Name":"TransactionDate","Value":20230709182426},{"Name":"PhoneNumber","Value":254769702562}]}}}}'

def save_data(body):
        data=json.loads(body)['Body']['stkCallback']
        if str(data['ResultDesc']).__contains__("successfully"):
            print("intiated")
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
            tans=models.Transactions(transaction_code=transaction_code,merchant_id=merchant_id,Phone_number=PhoneNumber,Checkout_id=checkout_id,Amount=Amount,date_transacted=date_transacted,completed="Completed")
            if tans.save():
                print("Transaction saved successfully")

save_data(body)
    
 