
import unittest
from otp_manager import OTPManager
import boto3  # Import the Boto3 library for the AWS service you are mocking (e.g., DynamoDB, SNS)
from botocore.stub import Stubber
import json
from boto3.dynamodb.types import TypeSerializer
from unittest.mock import patch



class TestRequest(unittest.TestCase):

    def test_save_otp(self):
        with patch('data_manager.DataManager.store_otp_data') as mock_function:
            mock_function.return_value = True
            otpm = OTPManager()
            result = otpm.save_otp("key_1", "0412345678")
            self.assertTrue(result)

    def test_get_otp(self):
        with patch('data_manager.DataManager.load_otp_data') as mock_function:
            mock_function.return_value = "0412345678"
            otpm = OTPManager()
            result = otpm.get_otp("key_1")
            self.assertEquals(result, "0412345678")

if __name__ == "__main__":
    unittest.main()
