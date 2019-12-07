from rtk8s.rendering import render_project

# conf_path = ".rtk8s_apps/v1/{name}/conf.yml"
# config = json.load(open(conf_path))

config = {"service": {"name": "proxima"}}

name = config["service"]["name"]

render_project("rtk8s/templates/v1/service/",
               f".rtk8s_apps/v1/{name}/service",
               config)
