#!/usr/bin/env python

import sys
import yaml
import pprint
import jinja2
import glob
import re

TEMPLATE_FILE = "template/template.html"
OUTPUT_DIR = "output/"
SUFFIX = "-service.html"

def process_service_definition(template, service):
    
    data = yaml.safe_load(open(template, 'r'))

    templateLoader = jinja2.FileSystemLoader(searchpath = "./")

    env = jinja2.Environment(loader = templateLoader)

    template = env.get_template(TEMPLATE_FILE)
    output = template.render(data)

    output_file = OUTPUT_DIR + service + SUFFIX
    of = open(output_file, 'w')
    of.write(output)
    print('Wrote %s ' % output_file)

if __name__ == "__main__":

    templates = glob.glob('services/*-service.yml')

    for tmpl in templates:
        service = re.search("services/(.*)-service.yml", tmpl).group(1)
        print("Processing: %s " % service)
        process_service_definition(tmpl, service)