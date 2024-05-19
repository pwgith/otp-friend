import json

class OTPException(Exception):
    pass

class OTPInvalidDataElement(OTPException):
    def __init__(self, data_element):
        self.data_element = data_element

class OTPDataException(OTPException):
    pass

class OTPDataNotFound(OTPDataException):
    def __init__(self, otp_key):
        self.otp_key = otp_key

