# Deploying an App

This document outlines how to go about deploying a new application. It assumes you've [configured the environment]() correctly
and have [created a deployment](). This document assumes there's a deployment named `smeiling`. Confirm this by checking
the path `rtk8s_apps/v1/smeiling` exists.

## Adding an App

The first step is to add the app to the deployment's registry. This will make the deployment 'aware' of the application,
but won't deploy it yet. To do this, run:

`rtkctl add {app-name} smeiling`

Where `{app-name}` should refer to the name of your application and _should be all lower case_.

Navigate to `rtk8s_apps/v1/smeiling/registry/{app-name}.json`. This is your app's basic configuration. Fill this out
to prepare your app for deployment. An example file can be found below.

Note that you can also use a template config file of your own (maybe with standard settings in it, for example) with:

`rtkctl add {app-name} smeiling -c {your-config}.json`

You may still need to manually edit the app's config depending on the provided config. 

The tool accepts both `YAML` and `JSON` formatted files as template configurations.

## Deploying the App

With your config file filled out, you can now move to deployment. You can do this with:

`rtkctl deploy {app-name} smeiling`

This does the following:

1. Generates the app's source code and config files.
2. Builds the app's Docker images.
3. Pushes the app's Docker images to a specified Docker repository.
4. Configures the target Kubernetes cluster.

When finished, you should see a directory at `rtk8s_apps/v1/smeiling/src/{app-name}`. In here, you'll see two subdirectories
`app` and `proxy`. The `app` directory contains the source code for your app's frontend, while the `proxy` directory 
contains the code for your app's Splunk proxy service that enables SSL in the frontend.

After a minute or two, you should be able to navigate to `https:/{your-host-address}/{app-name}-app` and see you app!

If you want to make changes to the configuration and redeploy the app, you can run:

`rtkctl deploy {app-name} smeiling --overwrite --rebuild`

or more succinctly:

`rtkctl deploy {app-name} smeiling -O -R`

This will regenerate all application code, and rebuild your containers. If you wish to update the cluster specs only,
you can run:

`rtkctl deploy {app-name} smeiling`

As normal. Any changes will be _applied_ to the cluster.

Finally, it is generally recommended that you do not change the source code of an app, and make any changes to your app through 
the app's core config in the `registry` directory. Any changes to the source code _may result in unsynchronised app
configurations_. This will not break the app, but may have unintended consequences.

## Removing an App

You may want to remove your app from the cluster. `RTK8S` supports two main uses cases:

1. Removing the app from the cluster, but preserving its core configuration (in `rtk8s_apps/v1/smeiling/registry`).

`rtkctl remove {app-name} smeiling`

2. Removing the app from the cluster, but deleting all configuration too.

`rtkctl remove {app-name} smeiling --clean-all`

_Note that all actions are irreversible_.

## Example Config File

This is a simple example of an app config file:

```yaml
version: "beta"

app:
  name: "demo"
  host: "34.70.106.1"
  port: "80"
  scheme: "https"

  dashboards:
    Vodafone:
      app: "rot_smart_homes_app"
      name: "smeiling_dashboard_vodafone_demo_v10"

  splunk:
    host: "127.0.0.1"
    port: "8000"
    scheme: "http"
    username: "demodash"
    password: "****"

  style:
    logos:
      smeiling: "app/SmEILing.png"
      republic: "app/republic_logo.png"
      partner: "app/republic_logo.png"

    stylesheets:
      - "app/content/republic.css"

  deployment:
    repo: "localhost:32000"
```

What have we got here? 

All data related to the app _must_ be under the `app` key. At present, there are the following keys:

* `name` - The name of your app! In this case it's `demo`.
* `host` - The host for your app. This could be an IP or domain name.
* `port` - The port your app will be exposed on. This should be `"80"`.
* `scheme` - The scheme to use when handling requests. This should be `"https"`.
* `dashboards` - The metadata associated with the Splunk dashboard/s you wish to display. This example has only one dashboard enabled '`Vodafone`'. You could add another like:

```yaml
    dashboards:
        Vodafone:
          app: "rot_smart_homes_app"  # this is the application name.
          name: "smeiling_dashboard_vodafone_demo_v10"   # this is the dashboard name.
        Enofadov:  # keep adding new keys to be new dashboards
          app: "rot_smart_homes_app"
          name: "smeiling_dashboard_enofadov_demo_v10"
```

* `splunk` - The configuration settings for your Splunk instance! This _must_ include the five fields shown above.
* `style` - This key points to style information for the app. You can customise logos and CSS here.
* `deployment` - This points to various bits of info relevant to deploying the app. Here we see `repo`, the address of the Docker repository you'll be pushing to/pulling from.
