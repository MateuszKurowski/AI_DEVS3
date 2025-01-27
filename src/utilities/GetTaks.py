import requests

def get_task(task_name: str, url: str = 'https://centrala.ag3nts.org/'):
    url = url + task_name
    session = requests.Session()
    response = session.get(url)
    response.raise_for_status()
    return response
