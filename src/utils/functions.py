import json, re, os, dotenv, chalk
from datetime import datetime
from src.constants.icons import icons
import facebook

def json_decode(pathfile):
    result = None
    try:
        with open(pathfile, "r") as file:
            try:
                result = json.loads(file.read())
                file.close()
            except Exception:
                print("invalid json file")
                return
    except IOError:
        print(f"file at { pathfile } doesn't exist")
        return
    
    return result

def json_encode(data):
    try:
        return json.dumps(data)
    except Exception:
        raise "failed when convert to json"

def text_split(text):
    pattern = r"(\,|\|)"
    items = list( filter(lambda item: re.match(pattern, item) == None, list(map(lambda item: str(item).strip(), re.split(pattern, text)))) )
    return items

def url_join (domain, username):
    return f"https://{ domain }/{ username }"

def get_class_attribute (C, method):
    name = C.__name__
    registry = { f"{name}": C }
    return getattr(registry[name], method)

def now ():
    return datetime.now().strftime("%H:%M:%S")

def date ():
    time = datetime.now()
    return f"{ time.day }-{ time.month }-{ time.year }"

def user_input (text, icon):
    return input(f"{ icons[icon] } { text } : ")

def env (key, alternative = None):
    file = dotenv.find_dotenv()
    dotenv.load_dotenv(file)
    item = os.environ.get(key) if not os.environ.get(key) == None else alternative
    if item == None:
        os.environ[key] = user_input(f"input variabel { key }", "input")
        dotenv.set_key(file, key, os.environ[key])
        return os.environ[key]
    else:
        return item

def write (text, icon):
    print (f"{ icons[icon] } { text }")

def GraphApi_login (token):
    try:
        return facebook.GraphAPI(access_token=token)
    except Exception as e:
        print (e)
        return False
def typeof (_any_):
    return type(_any_).__name__

def dict_show (items):
    for key in items:
        if key in items:
            if typeof(items[key]) != "dict":
                write(f"{key} : { chalk.cyan(items[key]) }", "info")
            else:
                dict_show(items[key])

def loop (char, each):
    result = str(char)
    for x in range (each):
        result += char
    return result

