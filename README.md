## locafan
=======

TCC LOCAFAN - EaD Técnico em Informática - CEPSS

## usage
=======
Execute em um terminal de qualquer distribuição GNU/Linux baseada em Debian Wheezy:

    git clone https://github.com/jmanoel7/locafan.git
    cd locafan/scripts
    ./install-deps.sh
    ./install-venv.sh
    cd ..
    source ~/.local/venvs/locafan/bin/activate
    python manage.py syncdb
    python manage.py runserver

Se deu tudo certo, abra agora um web browser no endereço:

**http://localhost:8000/**

## TODO:
=======
* Terminar a APP: 'clientes'
* Desenvovler as APPs: 'fantasias' e 'locacoes'
* Customizar com JQuery-UI o site LocaFan
