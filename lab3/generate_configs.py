import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML
with open("routers.yaml") as f:
    data = yaml.safe_load(f)

# Load template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("router_config.j2")

# Generate configs
for hostname, router_data in data["routers"].items():

    config = template.render(
        hostname=hostname,
        router_id=router_data["router_id"],
        interfaces=router_data["interfaces"],
        ospf=router_data["ospf"]
    )

    with open(f"{hostname}.cfg", "w") as f:
        f.write(config)

    print(f"Generated {hostname}.cfg")
