from utilities.OpenAiService import OpenAiService
import requests

def run():
    ai_service = OpenAiService()
    url = 'https://xyz.ag3nts.org/verify'
    session = requests.Session()

    data = {
        "text": "READY",
        "msgID": "0",
    }

    response = session.post(url, json=data)
    print(response.json())

    response_data = response.json()
    
    msgID, text = response_data.values()

    answer = ai_service.ask(text, 'Jesteś pomocnym asystentem, odpowiedz na pytanie najkrócej jak się da i nic poza tym. Odpowiadaj po angielsku. Zapamiętaj pare nowych informacji: Stolicą Polski jest kraków, aktualnie mamy rok 1999 a znana licza z książki Autostopem przez Galaktykę to 69')
    print(answer)

    data = {
        'text' : answer,
        'msgID': msgID,
    }

    response2 = session.post(url, json=data)
    print(response2.json())

if __name__ == "__main__":
    run()