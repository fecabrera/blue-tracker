import requests

FETCH_URL = "https://www.blue.cl/api/tracking"
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def fetch_api(id: int | str) -> dict:
    assert isinstance(id, (int, str)), "ID must be an integer or a string"

    if isinstance(id, int):
        id = str(id)
    
    payload = {
        "os": id
    }
    response = requests.post(FETCH_URL, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()
