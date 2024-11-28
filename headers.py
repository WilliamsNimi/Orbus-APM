import requests
import os

token = os.environ['BearerToken']
url = "https://sterlingbank-api.iserver365.com/odata/Objects"
headers = {
	"content-type": "application/json",
	"Authorization": f"Bearer {token}"
}
req = requests.get(url, headers=headers)
print(req.content)