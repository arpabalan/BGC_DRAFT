
import requests
import json

def device_Start():
    login_url = 'http://172.20.10.3/api/auth/login'
    cred = '{"username":"admin","password":"eve", "html5":"-1"}'
    headers = {'Accept': 'application/json'}

    login = requests.post(url=login_url, data=cred)
    cookies = login.cookies
    print('Starting device')

    starting_node_url = f'http://172.20.10.3/api/labs/netmiko_DCLAB/Test_lab2.unl/nodes/1/start'
    print(type(starting_node_url))
    start_node_api = requests.request('GET', starting_node_url, headers=headers, cookies=cookies)
    print(start_node_api.json())


device_Start()
