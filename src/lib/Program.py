from .Interface import Interface
from .HumanFinder import HumanFinder
from src.constants.layouts import barrier
from src.utils.functions import text_split

class Program:
    def __init__(self):
        pass
    
    @staticmethod
    def mainTask():
        data = {}
        targets = text_split(Interface.input("input username target", "question"))
        for username in targets:
            print (f"{ barrier } { username } { barrier}")
            target = HumanFinder(username)
            informations = target.getInformations()
            
        
    @staticmethod
    def start():
        Interface.show()
        Program.mainTask()