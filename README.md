## locafan
=======

TCC LOCAFAN - EaD Técnico em Informática - CEPSS

## usage
=======
Execute em um terminal de qualquer distribuição GNU/Linux baseada em Debian Wheezy:

    git clone https://github.com/jmanoel7/locafan.git
    cd locafan/scripts
    ./install-deps-debian-7.sh # ou ./install-deps-ubuntu-1404.sh
    ./install-venv.sh
    cd ..
    source ~/.local/venvs/locafan/bin/activate
    python manage.py syncdb # na pergunta que se fizer em seguida a este comando, responda: 'no' (sem as aspas)
    python manage.py runserver

Se deu tudo certo, abra agora um web browser no endereço:

**http://localhost:8000/**

## TODO:
=======
* Finalizar correção de bugs
