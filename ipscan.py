import requests
import json
import time
	#store API key
headers = ('API-Key' : '$api-key', 'Content-Type':'application/json')
	#take the URL for scanning
data = {"url": "https://66.175.56.206/", "visibility": "public"}
	#search the url
response = requests.post("https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data))
	#parse the UUID
uuid = (response.json()['uuid'])
	#print it to the console
print(uuid)
	#wait 5 seconds
time.sleep(5)
	#pump uuid into api to get results of the scan
result_url = f'https://urlscan.io/api/v1/result/{uuid}/'
result = requests.get(result_url)
	#put it into readable json format
result_data = result.json()
	#list json
print(list(result_data))
print(result)
	#parse for verdicts
print(result_data['verdicts'])