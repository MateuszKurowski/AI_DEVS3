import requests
from bs4 import BeautifulSoup
from utilities.OpenAiService import OpenAiService

ai_service = OpenAiService()

url = 'https://xyz.ag3nts.org/'
session = requests.Session()
response = session.get(url)

soup = BeautifulSoup(response.text, "html.parser")
question  = soup.find("p", id="human-question")
print(f'Pytanie: {question.getText()}')

userPrompt = "Odpowiedz na zamieszczone poniżej pytanie, odpowiedz tylko i wyłącznie cyfrą i niczym więcej: ### " + question.getText()
ai_response = ai_service.ask(userPrompt)

print(f'Odpowiedź: {ai_response}')

data = {
    "username": "tester",
    "password": "574e112a",
    "answer": str(ai_response),
}

response2 = session.post(url, data)
soup = BeautifulSoup(response2.text, "html.parser")

if response2.status_code == 200:
    print("Odpowiedź serwera:", soup.prettify())
else:
    print("Wystąpił błąd:", response2.status_code, response2.text)