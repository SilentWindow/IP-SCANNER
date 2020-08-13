
import requests
import json
import time
	#store API key
headers = {'API-Key' : 'd0b16e47-5bb2-45ed-89c0-93b593a6aedc', 'Content-Type':'application/json'}

with open ("TextFile1.txt") as myfile:
	reed = [line.rstrip() for line in myfile]

s = 0

for x in range(len(reed)):
	data = {"url": reed[s], "visibility": "public"}

while s < len(reed):
	response = requests.post("https://urlscan.io/api/v1/scan", headers=headers, data=json.dumps(data))	
	#parse the UUID
	uuid = (response.json()['uuid'])
	#print it to the console
	url = (response.json()['url'])
	print(url)
	print("the UUID:")
	print(uuid)
	#wait 5 seconds
	print("loading...")
	time.sleep(30)
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
	print('\n')
	s = s + 1
