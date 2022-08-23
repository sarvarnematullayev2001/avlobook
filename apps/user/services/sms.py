import requests
from requests.auth import HTTPBasicAuth

from config.settings import SMS_LOGIN, SMS_PASSWORD


def send_phone_sms_code(phone_number: str, code: str):
    API = "http://91.204.239.44/broker-api/send"
    data = {
        "messages":
            [
                {
                    "recipient": phone_number.replace('+', ''),
                    "message-id": "nov03145948g9",
                    "sms": {
                        "originator": "3700",
                        "content": {
                            "text": code
                        }
                    }
                }
            ]
    }
    auth = HTTPBasicAuth(username=SMS_LOGIN, password=SMS_PASSWORD)
    requests.post(auth=auth, json=data, url=API)
