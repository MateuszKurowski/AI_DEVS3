import requests
from dotenv import load_dotenv
import os
import json

def send_task(answer: str, task_name: str, url: str = 'https://centrala.ag3nts.org/report'):
    load_dotenv()
    ai_devs_key = os.getenv('ai_devs_key')

    data = {
        "task": task_name,
        "apikey": ai_devs_key,
        "answer": answer
    }
    print('Dane: ' + json.dumps(data, indent=4))
    print()
    print(14 * '-')
    print()

    response = requests.post(url, json=data)

    print("Status code:", response.status_code)
    print("Odpowiedź serwera:", response.text)