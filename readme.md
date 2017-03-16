# API com Django Rest Framework e AngularJS

Esse é um projeto feito para aprimorar minhas skills com Django Rest e angularJS. Foram criados custom commands para automatizar alguns processos e todo codigo está alinhando com o style code do django e pep8.

## Setup

### Docker

```
docker-compose up
```

### Virtualenv

1. Criar virtualenv

        mkvirtualenv exampleAPI
        workon exampleAPI

2. Instalar dependências

        pip install -r requirements.txt
        python setup.py develop
        npm install -g grunt-cli bower

3. Instalar e compilar Assets

        npm install
        bower install
        grunt

4. Criar database e inserir dados

        make create_database; make make_fixtures

6. Iniciar servidor de desenv

        ./manage.py runserver
