# Creating a Deployment 

`rtkctl create {deployment-name} -k {tls-path}`

`rtkctl delete {deployment-name}`

## External access

`iptables -P FORWARD ACCEPT`
https://github.com/ubuntu/microk8s/issues/75