# Import libraries
from jinja2 import Environment, FileSystemLoader
import yaml

# Declare environment
ENV = Environment(loader=FileSystemLoader('.'))


# Custom filter function
def get_interface_speed(interface_name):

    """
    Return interface speed based on interface type
    """

    if 'gigabit' in interface_name.lower():
        return 1000

    if 'fast' in interface_name.lower():
        return 100


# Register filter
ENV.filters['get_interface_speed'] = get_interface_speed


# Load template
template = ENV.get_template("template-task8.j2")


# Load YAML data
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)


# Render template
print(template.render(interface_list=interfaces))
