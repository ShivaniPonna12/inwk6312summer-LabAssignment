from jinja2 import Environment, FileSystemLoader
import yaml

# Load templates
ENV = Environment(loader=FileSystemLoader('.'))

# Load template
template = ENV.get_template("template-task6.j2")

# Open YAML file
with open("data-task7.yml") as f:

    # Convert YAML into Python objects
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# Render template
print(template.render(interface_list=interfaces))
