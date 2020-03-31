import requests
import json

ip = input('Enter the IP address : ')
response = requests.get('http://ip-api.com/json/' + ip + '?fields=16921')
response.text
locn = response.json()
if locn['status'] == 'success':
    print('\n\n')
    print(f'ISP     : {locn["isp"]}')
    print(f'region  : {locn["regionName"]}')
    print(f'city    : {locn["city"]}')
    print(f'country : {locn["country"]}')
    print('\n')
else:
    print('\nNo info Found about this IP\n')
