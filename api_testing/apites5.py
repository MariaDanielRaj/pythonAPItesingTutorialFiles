
import requests

url = "https://www.hackthis.co.uk/?login"
resp = requests.post(url=url,data={'username':'test7901','password':'test7902'})
print('Logout' in resp.text)
