import requests
import json
from pprint import pprint

resp=requests.get('https://reqres.in/api/users?page=2')

#import ipdb; ipdb.set_trace()
pprint(resp.json())

#res = json.dumps(resp.json(),indent=4)

print(res)
