# RTK8S

## Getting Started

Before deploying any applications, you'll need to configure the basic infrastructure to deploy your applications into. 
To do this, you'll need to create the 'Deployment'. A 'Deployment' can have zero or more apps associated with it. It 
defines security and routing for these apps. If you can see `.rtk8s_apps/v1/smeiling` u

You'll need to have `kubectl` installed to get started. To check if this is installed, run 
`kubectl config current-context ` in your shell. This should return `...`

Next you can 

## Deploying an Application

### 1. Add

```rtkctl add {app} {deployment}```

```.rtk8s_apps/v1/{deployment}/registry/{app}.json```

```rtkctl add {app} {deployment} -c config.yml```

### 2. Deploy

```rtkctl deploy {app} {deployment}```

### 3. Remove

```rtkctl remove {app} {deployment}```

## The Nuclear Option

```rtkctl delete {deployment}```
