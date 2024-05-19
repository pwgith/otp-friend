from decimal import Decimal
import json
import time
import random


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def generate_new_id():
    timestamp = str(int(time.time() * 1000))  # Convert current timestamp to milliseconds
    random_number = str(random.randint(0, 9999)).zfill(4)  # Generate a random 4-digit number
    unique_id = timestamp + random_number
    return unique_id