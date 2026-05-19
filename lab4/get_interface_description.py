from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
    }
]

for device in devices:
    net_connect = ConnectHandler(**device)

    print("\n" + "=" * 80)
    print(f"INTERFACE DESCRIPTION for {device['ip']}")
    print("=" * 80)

    output = net_connect.send_command("show interface description")

    print(output)

    net_connect.disconnect()
