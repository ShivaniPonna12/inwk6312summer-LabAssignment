from jinja2 import Environment, FileSystemLoader

# Load template environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task2.j2")


# Create interface class
class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink


# Create interface object
interface_obj = NetworkInterface(
    "GigabitEthernet0/1",
    "Server Port",
    10,
    True
)

# Render template
print(template.render(interface=interface_obj))
