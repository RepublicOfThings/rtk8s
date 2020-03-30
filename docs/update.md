# Updating Deployments

From time to time, it may be necessary to _update_ existing deployments.

Fortunately, `rtkctl` provides utility to help you do this. Be warned though: apps that
are being updated will be unavailable for up to 5 minutes.

## Updating one app

To update a single app (say `demo`), you can run:

```bash
rtkctl update smeiling -n demo
```

Just substitute `demo` for your app name. This will _remove all existing source code_
from the app's source directory. It will then regenerate this code from the app spec.
Finally, it'll rebuild the app's containers and deploy them into the cluster. After a
few moments you'll see that your app is back online.

## Updating all apps in a deployment

In the event of a software update, it may be necessary to roll out updates to all apps.

The `rtkctl` tool provides a utility to do this. While nothing should go wrong, it's 
always a good idea to **take a backup of your specs in the `registry` directory** before
proceeding.

When you're ready, run:

```bash
rtkctl update smeiling -A
```

You will be prompted to confirm your intention to update your deployment, hit `Y` if you
wish to proceed (note: you can run `rtkctl update smeiling -A -Y` to shortcut this).

You should see the tool begin to update and redeploy your apps to the latest info in 
the specs and in `rtk8s` itself.
