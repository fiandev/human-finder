from src.utils.functions import user_input
from src.constants.layouts import banner

class Interface:
    @staticmethod
    def input(text, icon = "question"):
        return user_input(text, icon)
        
    @staticmethod
    def show():
        print (banner)