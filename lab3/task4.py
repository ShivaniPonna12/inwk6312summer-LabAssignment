from jinja2 import Environment, FileSystemLoader

# Load template environment
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task4.j2")


# Define interface class
class NetworkInterface(object):

    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan


# Create object
interface_obj = NetworkInterface(
    "Server Port",
    10
)

# Render template
print(template.render(interface=interface_obj))
