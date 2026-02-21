import requests
from string import *


username = "natas23"
password = "dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs"
url = f"http://{username}.natas.labs.overthewire.org"


session = requests.Session()
response = session.post(url, auth=(username, password), data={"passwd": "20iloveyou"})
print(response.text)
print("Status code:", response.status_code)
