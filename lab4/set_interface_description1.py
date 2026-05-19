from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": 22},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": 22},
]

description = "Description set with Netmiko"

for device in devices:

    print(f"\nConfiguring {device['ip']}")

    net_connect = Netmiko(**device)

    config = [
        "interface GigabitEthernet3",
        f"description {description}"
    ]

    output = net_connect.send_config_set(config)

    print(output)

    net_connect.disconnect()
