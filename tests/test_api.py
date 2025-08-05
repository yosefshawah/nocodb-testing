import requests

BASE_URL = "http://localhost:8080"

def test_server_up():
    response = requests.get(BASE_URL)
    assert response.status_code == 200 or response.status_code == 302  # 302 if redirecting to /dashboard

def test_unauthorized_without_token():
    url = f"{BASE_URL}/api/v2/tables"
    response = requests.get(url)
    assert response.status_code == 401
    assert response.json().get("error") == "AUTHENTICATION_REQUIRED!!"
