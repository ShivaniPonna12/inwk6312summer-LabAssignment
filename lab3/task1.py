from jinja2 import Environment, FileSystemLoader

# Load templates from current directory
ENV = Environment(loader=FileSystemLoader('.'))

# Load the template file
template = ENV.get_template("template.j2")


# Create a Python class
class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink


# Create an object
interface_obj = NetworkInterface(
    "GigabitEthernet0/1",
    "Server Port",
    10
)

# Render template with object data
print(template.render(interface=interface_obj))

