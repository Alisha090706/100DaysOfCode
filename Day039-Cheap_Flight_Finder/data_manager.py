import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint = SHEET_ENDPOINT
        self.headers = {
            "Authorization": f"Bearer {os.getenv('TOKEN')}"
        }
    def get_data(self):
        response = requests.get(url= self.sheet_endpoint, headers= self.headers)
        response.raise_for_status()
        data = response.json()
        return data 
    def add_data(self,new_data):
        sheet_input = {
            "price": new_data
        }
        response = requests.post(url= self.sheet_endpoint, json= sheet_input, headers= self.headers)
        response.raise_for_status()
        return response.json()
    def update_data(self, row_id, updated_data):
        sheet_input = {
            "price": updated_data
        }
        response = requests.put(url= f"{self.sheet_endpoint}/{row_id}", json= sheet_input, headers= self.headers)
        response.raise_for_status()
        print(response.text)
        return response.json()
    def delete_data(self, row_id):
        response = requests.delete(url= f"{self.sheet_endpoint}/{row_id}", headers= self.headers)
        response.raise_for_status()
        return response.status_code