import requests
from string import *


username = "natas22"
password = "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz"
url = f"http://{username}.natas.labs.overthewire.org/?revelio=true"


session = requests.Session()
response = session.get(url, auth=(username, password), allow_redirects=False)
print(response.text)
print("Status code:", response.status_code)
