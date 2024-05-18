"""os module to get env vars"""
import os
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './src')
os.environ["PYTHONPATH"] = os.environ["PYTHONPATH"] + ":" + src_path

import json
import logging
from otp_manager import OTPManager

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
    request_id = event["requestContext"]["requestId"]
        
    otp = message
    try:
        otpManager = OTPManager()
        result = otpManager.saveOTP(otp)
        return {'statusCode': 200, 'body': "OTP has been saved"}
    except Exception as e:
        logging.exception("Error savibg OTP %s", str(e))        
        return {'statusCode': 500, 'body': 'Was unable to save OTP in the database: ' + e.__str__()}

