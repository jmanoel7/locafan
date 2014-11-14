#!/bin/bash -e
mkdir -p ~/.local/venvs
virtualenv --no-site-packages ~/.local/venvs/locafan
source ~/.local/venvs/locafan/bin/activate
pip install -r requirements.txt
exit 0
