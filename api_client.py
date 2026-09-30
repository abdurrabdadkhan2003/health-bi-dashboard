import os
import requests
from dotenv import load_dotenv

load_dotenv()

class MeditrackAPIClient:
    def __init__(self):
        self.base_url = os.getenv("API_URL", "http://localhost:8000")
        self.token = None

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/login", 
            data={"username": username, "password": password}
        )
        if response.status_code == 200:
            self.token = response.json().get("access_token")
            return True
        return False

    def _get_headers(self):
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}

    def get_patients(self):
        response = requests.get(f"{self.base_url}/patients", headers=self._get_headers())
        return response.json() if response.status_code == 200 else []

    def get_appointments(self):
        response = requests.get(f"{self.base_url}/appointments", headers=self._get_headers())
        return response.json() if response.status_code == 200 else []
        
    def get_visits(self):
        response = requests.get(f"{self.base_url}/visits", headers=self._get_headers())
        return response.json() if response.status_code == 200 else []