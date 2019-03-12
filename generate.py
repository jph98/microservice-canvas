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

def process_service_definition(s):
    
    data = yaml.safe_load(open(s, 'r'))

    templateLoader = jinja2.FileSystemLoader(searchpath = "./")

    env = jinja2.Environment(loader = templateLoader)

    template = env.get_template(TEMPLATE_FILE)
    output = template.render(data)

    of = open(OUTPUT_DIR + domain + SUFFIX, 'w')
    of.write(output)

if __name__ == "__main__":

    services = glob.glob('services/*-service.yml')

    for s in services:
        domain = re.search("services/(.*)-service.yml", s).group(1)
        print("Processing: %s " % domain)