import chalk
from .Interface import Interface
from .Crawler import Crawler
from .File import File
from src.constants.sites import sites
from src.constants.layouts import barrier
from src.constants.icons import icons
from src.constants.path import PATH_PROGRAM
from src.utils.functions import write, dict_show, url_join, get_class_attribute, date, now, json_encode

class HumanFinder:
    result = []
    photos = []
    posts = []
    avatars = []
    names = []
    
    def __init__(self, username):
        self.username = username
    
    def getInformations(self):
        username = self.username
        for key in sites:
            site_url = url_join(sites[key], username)
            crawler = get_class_attribute(Crawler, key)
            data = crawler(username)
            
            # interface result process
            if not data == False:
                print (f"{ icons['success'] } { key } with username { username } found !")
                self.result.append({
                  f"{ key }": data
                })
            else:
                print (f"{ icons['error'] } { key } with username { username } not found !")
            
            # end
        # show results
        for item in self.result:
            print (barrier)
            dict_show(item)
        
        # saving result
        dest = f"results/{ date() }/[{username}]_{ now() }.json"
        File.save(json_encode(self.result), f"{ PATH_PROGRAM }/{ dest }")
        
        print (f"{ icons['success'] } file of result saved at { dest }")