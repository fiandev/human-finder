from .API import API
from src.constants.sites import sites

class Crawler:
    @staticmethod
    def github (username):
        try:
            data = API.github(username)
            return data if data.get("message") == None else False
        except Exception as e:
            return False
        
    @staticmethod
    def twitter (username):
        return False
        
    @staticmethod
    def facebook (username):
        try:
            return API.facebook(username)
        except Exception as e:
            return False