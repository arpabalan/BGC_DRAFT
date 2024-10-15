import time

import requests
import json
import pprint
import re
from devnet_101_Starting_Devices import device_Start

login_url = 'http://172.20.10.3/api/auth/login'
cred = '{"username":"admin","password":"eve", "html5":"-1"}'
headers = {'Accept': 'application/json'}
login = requests.post(url=login_url, data=cred)
cookies = login.cookies
class Network_Device():
    def __init__(self, device_name, node_id=None):
        self.device_name = device_name
        self.node_id = node_id

    # creating device
    def creating_router_device(self):
        ios_router = {"template": "vios", "type": "qemu", "count": "1", "image": "vios-adventerprisek9-m.SPA.156-1.T",
                    "name": f"vIOS_API_{self.device_name}", "icon": "Router.png", "uuid": "", "cpulimit": "undefined",
                    "cpu": "1", "ram": "1024",
                    "ethernet": "4", "qemu_version": "", "qemu_arch": "", "qemu_nic": "",
                    "qemu_options": "-machine type: pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                    "ro_qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                    "config": "0", "delay": "0", "console": "telnet", "left": "592", "top": "129", "postfix": 0}


        ios_data = json.dumps(ios_router)
        create_url = 'http://172.20.10.3/api/labs/DEVNET_PRACTICE/BGC_DC_DRAFT.unl/nodes'
        create_api = requests.post(url=create_url, data=ios_data, cookies=cookies, headers=headers)
        response = create_api.json()
        print(response['data']['id'])
        self.node_id = response['data']['id']
        print(type(self.node_id))
        print("NODE ID: ", self.node_id )
        return self.node_id

    def creating_switch_device(self):
        ios_router = {"template": "viosl2", "type": "qemu", "count": "1", "image": "viosl2-adventerprisek9-m.03.2017",
                      "name": f"vIOS_API_{self.device_name}", "icon": "Switch L3.png", "uuid": "", "cpulimit": "undefined", "cpu": "1",
                      "ram": "1024", "ethernet": "8", "qemu_version": "", "qemu_arch": "", "qemu_nic": "",
                      "qemu_options": "-machine type: pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                      "ro_qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                      "config": "0", "delay": "0", "console": "telnet", "left": "649", "top": "132", "postfix": 0}

        ios_data = json.dumps(ios_router)
        create_url = 'http://172.20.10.3/api/labs/DEVNET_PRACTICE/BGC_DC_DRAFT.unl/nodes'
        create_api = requests.post(url=create_url, data=ios_data, cookies=cookies, headers=headers)
        response = create_api.json()
        print(response['data']['id'])
        self.node_id = response['data']['id']
        print(type(self.node_id))
        print("NODE ID: ", self.node_id )
        return self.node_id

    # connecting device to mgmt
    def connecting_device_to_mgmt(self):
        print("Connecting to Interface")
        connect_interface_url = f'http://172.20.10.3/api/labs/DEVNET_PRACTICE/BGC_DC_DRAFT.unl/nodes/{self.node_id}/interfaces'
        int_map = '{"0":"1"}'
        connect_interface_api = requests.put(url=connect_interface_url, data=int_map, cookies=cookies, headers=headers)
        print(connect_interface_api.json())

    # starting all devices
    def starting_all_device(self):

        print('Starting device')
        starting_node_url = f'http://172.20.10.3/api/labs/DEVNET_PRACTICE/BGC_DC_DRAFT.unl/nodes/start'
        print(type(starting_node_url))
        start_node_api = requests.request('GET', starting_node_url, headers=headers, cookies=cookies)
        print(start_node_api.json())



router1 = Network_Device(device_name="CORE1")
router1.creating_router_device()
router1.connecting_device_to_mgmt()

switches = ["EDGE_SW1", "EDGE_SW2", "ACC_SW1", "ACC_SW2"]
for x in switches:
    switch1 = Network_Device(device_name=x)
    switch1.creating_switch_device()
    switch1.connecting_device_to_mgmt()





