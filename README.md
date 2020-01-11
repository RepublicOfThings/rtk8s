# RTK8S

## Getting Started

## Installing RTK8S

Ensure you have Python >= 3.6.x on your system, and that this version of Python is set for the current user.

```git clone https://github.com/RepublicOfThings/rtk8s```

```cd rtk8s```

`pip install -r requirements.txt`

`python setup.py install`

`rtkctl`

```bash
Usage: rtkctl [OPTIONS] COMMAND [ARGS]...
```

## Creating a `deployment`

Before starting, you may need to create a new deployment (if no directories exist at `rtk8s_apps/v1/`).

To create a new deployment 

### 0.  

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

## Advanced Information

`sudo apt-get install snapd`

### Configuring MicroK8s

`sudo snap install microk8s --classic`

`sudo microk8s.status --wait-ready`

`sudo microk8s.enable dns dashboard registry`

`alias kubectl='microk8s.kubectl'`

`microk8s.stop`

`microk8s.start`

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Other Info

Before deploying any applications, you'll need to configure the basic infrastructure to deploy your applications into. 
To do this, you'll need to create the 'Deployment'. A 'Deployment' can have zero or more apps associated with it. It 
defines security and routing for these apps. If you can see `.rtk8s_apps/v1/smeiling` u

You'll need to have `kubectl` installed to get started. To check if this is installed, run 
`kubectl config current-context ` in your shell. This should return `...`
