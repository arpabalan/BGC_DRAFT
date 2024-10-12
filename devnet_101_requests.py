import requests
import json



def device_instance(no_of_devices):
    login_url = 'http://172.20.10.3/api/auth/login'
    cred = '{"username":"admin","password":"eve", "html5":"-1"}'
    headers = {'Accept': 'application/json'}

    login = requests.post(url=login_url, data=cred)
    cookies = login.cookies

    print(cookies)
    for i in range(1, no_of_devices+1):
        ios_data = {"template": "vios", "type": "qemu", "count": "1", "image": "vios-adventerprisek9-m.SPA.156-1.T",
                    "name": f"vIOS_API_{i}", "icon": "Router.png", "uuid": "", "cpulimit": "undefined", "cpu": "1", "ram": "1024",
                    "ethernet": "4", "qemu_version": "", "qemu_arch": "", "qemu_nic": "",
                    "qemu_options": "-machine type: pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                    "ro_qemu_options": "-machine type=pc,accel=kvm -serial mon:stdio -nographic -no-user-config -nodefaults -rtc base=utc -cpu host",
                    "config": "0", "delay": "0", "console": "telnet", "left": "592", "top": "129", "postfix": 0}


        ios_data = json.dumps(ios_data)
        create_url = 'http://172.20.10.3/api/labs/netmiko_DCLAB/DC_LAB_ANSIBLE.unl/nodes'

        create_api = requests.post(url=create_url, data=ios_data, cookies=cookies, headers=headers)

        response = create_api.json()
        print(response['data']['id'])
        node_id = response['data']['id']

        print("Connecting to Interface")

        connect_interface_url = f'http://172.20.10.3/api/labs/netmiko_DCLAB/DC_LAB_ANSIBLE.unl/nodes/{node_id}/interfaces'
        int_map = '{"0":"5"}'
        connect_interface_api = requests.put(url=connect_interface_url,data=int_map,cookies=cookies,headers=headers)
        print(connect_interface_api.json())


        print('Starting device')
        starting_node_url = f'http://172.20.10.3/api/labs/netmiko_DCLAB/DC_LAB_ANSIBLE.unl/nodes/2/start'
        start_node_api = requests.request('GET', starting_node_url,headers=headers,cookies=cookies)
        print(start_node_api.json())


device_instance(3)