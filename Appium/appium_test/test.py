import requests
result = {}
import json
data = None
files=None
headers = {'content-type': 'application/json'}
url="https://www.baidu.com/"
r = requests.post(url, files=files, data=data, verify=False, headers=headers)
result["status_code"] = r.status_code
print(r.status_code)
print(r.text)
if r.status_code == 200 and len(r.text) > 0:
    r.encoding = 'UTF-8'
    result = json.loads(r.text)
result["status_code"] = r.status_code
print(result)