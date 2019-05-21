import requests
from bs4 import BeautifulSoup
import re
session = requests.session()
resp = session.get("https://opensource-demo.orangehrmlive.com/")

soup = BeautifulSoup(resp.text, 'lxml')
csrf = soup.select('#csrf_token')[0].get('value')
print(csrf)

login_data = {
'actionID': '',
'hdnUserTimeZoneOffset': '5.5',
'_csrf_token': csrf,
'txtUsername': 'Admin',
'txtPassword': 'admin123',
'Submit': 'LOGIN'
}
resp = session.post('https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials', data=login_data)
print(resp.text)


#pat = re.compile(r'<input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token"')
#results = re.search(pat, resp.text)
#print(results.group(1))
