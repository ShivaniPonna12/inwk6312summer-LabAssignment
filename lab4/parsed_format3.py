from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
        "port": 22
    }
]

for device in devices:

    print("\n" + "=" * 60)
    print(f"Router: {device['ip']}")
    print("=" * 60)

    net_connect = Netmiko(**device)

    output = net_connect.send_command(
        "show ip route",
        use_textfsm=True
    )

    net_connect.disconnect()

    for route in output:

        protocol = route.get("protocol", "N/A")
        network = route.get("network", "N/A")
        distance = route.get("distance", "N/A")
        metric = route.get("metric", "N/A")

        print(f"{protocol:10} {network:18} {distance:5} {metric}")
