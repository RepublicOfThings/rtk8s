import os
import shutil
import jinja2


def render_string():
    jinja2.Environment().


def render_project(templates, target):
    for root, dirs, files in os.walk(templates):
        for file in files:
            src = os.path.join(root, file)
            dst = os.path.join(target, root.replace(templates, ""))

            with open(src, "r") as file:
                pass

# out = "./test"
# path = "rtk8s/templates/v1/service/"