"""os module to get env vars"""
import os
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './src')
os.environ["PYTHONPATH"] = os.environ["PYTHONPATH"] + ":" + src_path

import json
import logging
from otp_manager import OTPManager
from otp_exceptions import OTPDataNotFound
from helper import DecimalEncoder

def is_valid_json(json_string):
    """Check if the json string is acutally valid json"""
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False

def save_otp(event, context):
    """Process a request for otp"""
    print("Event:", event)
    if type(event) is not dict:
        return {'statusCode': 400, 'body': 'Event parameter is not a hash'}
    if "body" not in event:
        return {'statusCode': 400, 'body': 'Body field is not in the event hash'}
    message = event['body']
    if type(message) is not dict:
        if not is_valid_json(message):
            return {'statusCode': 400, 'body': 'Body field is not valid json or a hash'}
        else:
            message = json.loads(message)
            
    if "requestContext" not in event or "requestId" not in event["requestContext"]:
        return {'statusCode': 400, 'body': 'Event is missing Request Id'}
        
    otp = message
    try:
        otpManager = OTPManager()
        result = otpManager.save_otp(otp["otp_key"], otp["otp_data"])
        return {'statusCode': 200, 'body': json.dumps("OTP has been saved", cls=DecimalEncoder)}
    except Exception as e:
        logging.exception("Error savibg OTP %s", str(e))        
        return {'statusCode': 500, 'body': json.dumps('Was unable to save OTP in the database: ' + e.__str__(), cls=DecimalEncoder)}

def save_otp_okta(event, context):
    """Process a request for otp"""
    print("Event:", event)
    if type(event) is not dict:
        return {'statusCode': 400, 'body': 'Event parameter is not a hash'}
    if "body" not in event:
        return {'statusCode': 400, 'body': 'Body field is not in the event hash'}
    message = event['body']
    if type(message) is not dict:
        if not is_valid_json(message):
            return {'statusCode': 400, 'body': 'Body field is not valid json or a hash'}
        else:
            message = json.loads(message)
            
    if "requestContext" not in event or "requestId" not in event["requestContext"]:
        return {'statusCode': 400, 'body': 'Event is missing Request Id'}
        
    otp = message["data"]["messageProfile"]

    response = {
        "commands":[
            {
                "type":"com.okta.telephony.action",
                "value":[
                    {
                    "status":"SUCCESSFUL",
                    "provider":"Yaknow",
                    "transactionId":"SM49a8ece2822d44e4adaccd7ed268f954",
                    "transactionMetadata":"Duration=300ms"
                    }
                ]
            }
        ]
    }
    try:
        otpManager = OTPManager()
        otpManager.save_otp(otp["phoneNumber"], otp["otpCode"])
        return {'statusCode': 200, 'body': json.dumps(response, cls=DecimalEncoder)}
    except Exception as e:
        logging.exception("Error savibg OTP %s", str(e)) 
        error_response = {
            "error":{
                "errorSummary":"Failed to deliver SMS OTP to Yaknow",
                "errorCauses":[
                    {
                        "errorSummary": e.__str__(),
                        "reason":"Unable to process",
                        "location":"Australia"
                    }
                ]
            }
        }       
        return {'statusCode': 500, 'body': json.dumps(error_response, cls=DecimalEncoder)}

def get_otp(event, context):
    """Process a request for test data"""
    if type(event) is not dict:
        return {'statusCode': 400, 'body': 'Event parameter is not a hash'}
    print ("get values:", event)
    otp_key = event['pathParameters']['key']

    try:
        otpManager = OTPManager()
        otp_data = otpManager.get_otp(otp_key)
        return_body = {'otp_key' : otp_key, 'otp_data' : otp_data }
        return_body_json = json.dumps(return_body, cls=DecimalEncoder)
        return {'statusCode': 200, 'body': return_body_json}
    except OTPDataNotFound as e:
        reponse = "OTP Key: <"+ otp_key + "> was not found"
        return {'statusCode': 404, 'body': json.dumps(reponse, cls=DecimalEncoder)}
    except Exception as e:
        logging.exception("Error getting request %s", str(e))        
        return {'statusCode': 500, 'body': json.dumps('Was unable to complete this get: ' + e.__str__(), cls=DecimalEncoder)}

