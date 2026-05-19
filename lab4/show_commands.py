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
]

for device in devices:
    net_connect = ConnectHandler(**device)

    print("\n" + "=" * 80)
    print(f"ROUTER: {device['ip']}")
    print("=" * 80)

    # 1. Interface description
    print("\n--- SHOW INTERFACE DESCRIPTION ---")
    print(net_connect.send_command("show interface description"))

    # 2. Interface status summary
    print("\n--- SHOW IP INTERFACE BRIEF ---")
    print(net_connect.send_command("show ip interface brief"))

    # 3. Routing table
    print("\n--- SHOW IP ROUTE ---")
    print(net_connect.send_command("show ip route"))

    # 4. Version info
    print("\n--- SHOW VERSION ---")
    print(net_connect.send_command("show version"))

    net_connect.disconnect()
