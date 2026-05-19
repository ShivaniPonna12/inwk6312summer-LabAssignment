from netmiko import Netmiko

devices = [
    {"ip": "192.168.1.101", "username": "student", "password": "Meilab123", "device_type": "cisco_ios"},
    {"ip": "192.168.1.102", "username": "student", "password": "Meilab123", "device_type": "cisco_ios"},
    {"ip": "192.168.1.103", "username": "student", "password": "Meilab123", "device_type": "cisco_ios"},
    {"ip": "192.168.1.104", "username": "student", "password": "Meilab123", "device_type": "cisco_ios"},
]

for d in devices:

    net_connect = Netmiko(**d)

    routes = net_connect.send_command(
        "show ip route",
        use_textfsm=True
    )

    print("\n" + "="*50)
    print(f"Router {d['ip']}")

    for r in routes:
        print(r.get("protocol"), r.get("network"), r.get("distance"), r.get("metric"))

    net_connect.disconnect()
