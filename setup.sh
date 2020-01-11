#!/usr/bin/env bash
sudo apt-get install -y git snapd
sudo apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev \
                        libffi-dev libsqlite3-dev tk-dev

sudo apt-get install -y libpng-dev libfreetype6-dev

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv rehash

exec $SHELL

pyenv install 3.6.0
pyenv virtualenv 3.6.0 general
pyenv global general

git clone https://github.com/RepublicOfThings/rtk8s
cd rtk8s
pip install -r requirements.txt
python setup.py install
pyenv rehash
mv keys ../keys
cd ..

sudo apt-get update
sudo apt-get install docker.io
sudo usermod -aG docker $USER

sudo snap install microk8s --classic --channel=1.14/stable
sudo microk8s.status --wait-ready
sudo microk8s.enable dns dashboard registry ingress
alias kubectl='microk8s.kubectl'
sudo usermod -aG microk8s.kubectl $USER
sudo usermod -aG kubectl $USER

export KUBECTL=microk8s.kubectl
