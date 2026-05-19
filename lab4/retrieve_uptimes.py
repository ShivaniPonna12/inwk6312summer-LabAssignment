from netmiko import Netmiko

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
    }
]

for device in devices:

    net_connect = Netmiko(**device)

    output = net_connect.send_command("show version")

    print("=" * 60)
    print(f"Router: {device['ip']}")

    # Split output into lines
    lines = output.splitlines()

    for line in lines:

        if "uptime is" in line:
            print("UPTIME:", line)

        if "Configuration register is" in line:
            print("CONFIG REGISTER:", line)

    net_connect.disconnect()
