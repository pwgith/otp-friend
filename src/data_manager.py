import json
import boto3
import os
from otp_exceptions import OTPDataNotFound, OTPInvalidDataElement

class DataManager:
    def __init__(self):
        self.dynamodb_resource = boto3.resource('dynamodb')

    def load_otp_data(self, otp_key):
        if otp_key is None:
            raise OTPInvalidDataElement("otp_key", otp_key)
        table = self.dynamodb_resource.Table('otpStore')
        query_key = {'otp_key': otp_key}
        response = table.get_item(Key=query_key)
        # Todo need a none data error here
        item = response.get('Item')
        otp_key = item["otp_data"]
        return otp_key

    def store_otp_data(self, otp_data):
        table = self.dynamodb_resource.Table('otpStore')
        result = table.put_item(Item=otp_data)
        return result
