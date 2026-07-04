import requests

from config import ACCESS_TOKEN
from config import PHONE_NUMBER_ID


def send_message(to, message):

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    return response.json()