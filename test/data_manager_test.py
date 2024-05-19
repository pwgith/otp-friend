import unittest
from data_manager import DataManager
import boto3 
from botocore.stub import Stubber
import json
import os

class TestStoreDataItem(unittest.TestCase):

    def test_load_otp(self):
        dynamodb_resource = boto3.resource("dynamodb")
        stubber = Stubber(dynamodb_resource.meta.client)
        dynamodb_data = {
            "otp_key" : {"S": "0412345678"}, 
            "otp_data" : {"S": "123456"}
        }

        stubber.add_response('get_item', {'Item': dynamodb_data})
        stubber.activate()


        dm = DataManager()
        dm.dynamodb_resource = dynamodb_resource
        returned_test_data = dm.load_otp_data("0412345678")

        expected_result = "123456"
        

        self.assertEqual(returned_test_data, expected_result)

    def test_store_built_data_item(self):
        dynamodb_resource = boto3.resource("dynamodb")
        stubber = Stubber(dynamodb_resource.meta.client)
        response = {
            'ResponseMetadata': {
                'HTTPStatusCode': 200
            }
        }

        stubber.add_response('put_item', response)
        stubber.activate()

        hash_data = {
            "otp_key" : "0412345678", 
            "otp_data" : "123456"
        }

        dm = DataManager()
        dm.dynamodb_resource = dynamodb_resource
        actual_result = dm.store_otp_data(hash_data)
        expected_result = {'ResponseMetadata': {'HTTPStatusCode': 200}}
        self.assertEqual(actual_result, expected_result)

