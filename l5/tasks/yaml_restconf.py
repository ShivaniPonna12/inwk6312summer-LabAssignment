import yaml
import json
import requests
import logging

from requests.auth import HTTPBasicAuth

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

USER = "student"
PASS = "Meilab123"

HEADERS = {
    "Accept": "application/vnd.yang.data+json",
    "Content-Type": "application/vnd.yang.data+json"
}

with open("routers.yaml") as f:
    config = yaml.safe_load(f)

for router in config["routers"]:

    host = router["mgmt_ip"]

    logging.info(f"Connecting to {router['hostname']} ({host})")

    base_url = f"http://{host}/restconf/api/running/interfaces/interface/"

    for interface in router["interfaces"]:

        interface_name = interface["name"]

        url = base_url + interface_name

        payload = {
            "ietf-interfaces:interface": {
                "name": interface_name,
                "description": "Configured using RESTCONF YAML",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": True,

                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": interface["ip"],
                            "netmask": interface["netmask"]
                        }
                    ]
                },

                "ietf-ip:ipv6": {}
            }
        }

        response = requests.put(
            url,
            auth=HTTPBasicAuth(USER, PASS),
            headers=HEADERS,
            data=json.dumps(payload)
        )

        if response.status_code == 204:

            logging.info(
                f"{router['hostname']} {interface_name} configured successfully"
            )

        else:

            logging.error(
                f"Failed on {router['hostname']} {interface_name}"
            )

            print(response.text)
