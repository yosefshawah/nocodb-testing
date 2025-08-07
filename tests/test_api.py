import requests
#testing automated CD
BASE_URL = "http://52.18.93.49:8080/"

class TestServerHealth:
    def test_server_up(self):
        response = requests.get(BASE_URL)
        assert response.status_code in (200, 302)  # 302 if redirecting to /dashboard
