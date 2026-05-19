import yaml
import logging
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# ---------------- Logging ----------------
logging.basicConfig(
    filename="network_deploy.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Load YAML ----------------
with open("network.yml") as f:
    data = yaml.safe_load(f)

# ---------------- Jinja2 Setup ----------------
env = Environment(loader=FileSystemLoader("."), trim_blocks=True)
template = env.get_template("config_template.j2")

# ---------------- Loop Devices ----------------
for device in data["devices"]:

    try:
        logging.info(f"Connecting to {device['name']} ({device['ip']})")

        net_connect = Netmiko(
            host=device["ip"],
            username=device["username"],
            password=device["password"],
            device_type=device["type"]
        )

        # Render config
        config = template.render(device=device).split("\n")

        # Push config
        output = net_connect.send_config_set(config)

        logging.info(f"Config pushed successfully to {device['name']}")
        print(f"Configured {device['name']} successfully")

        net_connect.disconnect()

    except Exception as e:
        logging.error(f"Error on {device['name']}: {str(e)}")
        print(f"Failed on {device['name']}")
