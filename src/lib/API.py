import requests
from facebook_scraper import get_profile
from src.utils.functions import json_decode, user_input, write

class API:
    @staticmethod
    def github (username):
        url = f"https://api.github.com/users/{ username }"
        response = requests.get(url)
        return response.json()
        
    def facebook (username):
        data = get_profile(username)
        if data["Name"] != "Konten Tidak Ditemukan":
            return data
        else:
            return False