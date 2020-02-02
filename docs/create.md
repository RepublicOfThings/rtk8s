# Creating a Deployment 

`rtkctl create {deployment-name} -k {tls-path}`

`rtkctl delete {deployment-name}`

## External access

`iptables -P FORWARD ACCEPT`
https://github.com/ubuntu/microk8s/issues/75

## SSL Certificate issues

If the deployment continues to use the K8s SSL certs, you'll need to rebuild the secret with:

```bash

```

You'll then need to delete the ingress:

```bash

```

The ingress should auto-heal and be available again after a few moments.
