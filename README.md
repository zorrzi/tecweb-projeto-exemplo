# 2023.2-tecweb-django-many-to-one-example
Repositório contém exemplo de relação Many-to-one

- Crie um ambiente virtual
- Ative o ambiente virtual
- Instale o Django
- Rode os seguintes comandos

        python manage.py migrate
        python manage.py loaddata dados-iniciais.json

- Em seguite, rode:

        python manage.py runserver

- Acesse: [http://localhost:8000/](http://localhost:8000/)

- Na página, clique em: `Criar um livro para este escritor`
    - Este link chamará a função `views.exemplo`. Veja o que a função está fazendo.
    Este é um bom exemplo para auxiliar o desenvolvimento da etapa de criação de Tags

Neste projeto de exemplo, existem dois modelos: `Escritor` e `Livro`.
Assim, podemos utilizar a relação de banco de dados um para muitos, onde um escritor pode estar vinculado a vários livros e um livro está vinculado a apenas um escritor.

___

## Outro exemplo

A documentação oficial do Django apresenta um exemplo que pode ser acessa em: [Documentação Oficial Django - Many-to-one](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/)

