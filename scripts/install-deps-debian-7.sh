#!/bin/sh -e
echo 'deb http://nginx.org/packages/debian/ wheezy nginx' | sudo tee /etc/apt/sources.list.d/nginx.list
echo 'deb-src http://nginx.org/packages/debian/ wheezy nginx' | sudo tee -a /etc/apt/sources.list.d/nginx.list
wget -q -O- http://nginx.org/keys/nginx_signing.key | sudo apt-key add -
sudo apt-get clean
sudo apt-get update
sudo apt-get install \
    devscripts \
    build-essential \
    git-core \
    git-doc \
    git-gui \
    libgraphviz-dev \
    graphviz \
    dia \
    dia-libs \
    dia-shapes \
    dia2code \
    nginx \
    nginx-debug \
    nginx-nr-agent \
    sqlite3 \
    sqlite3-doc \
    libsqlite3-dev \
    python-pysqlite2 \
    python-dev \
    virtualenvwrapper \
    python-virtualenv \
    python-pip \
    python-setuptools
exit 0
