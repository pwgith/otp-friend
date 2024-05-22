import datetime
from data_manager import DataManager

class OTPManager:
    def __init__(self):
        self.data_manager = DataManager()

    def save_otp(self, otp_key, otp_data):
        hash_data = {
            "otp_key" : otp_key,
            "otp_data" : otp_data
        }
        return self.data_manager.store_otp_data(hash_data)

    def get_otp(self, otp_key):
        otp_data = self.data_manager.load_otp_data(otp_key)
        return otp_data
    
    def get_otp_from_email(self, email):
        otp_result = "Nah"
        return otp_result

