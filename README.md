
Projeto- Petshop

Este projeto é um sistema desenvolvido em Django para o gerenciamento de um Petshop, permitindo o cadastro e administração de donos e seus respectivos animais de estimação.

- Integrantes
Gleison Carneiro

Israel Alves

📝 Descrição do Projeto
O sistema tem como objetivo facilitar a organização de um Petshop. Através do portal administrativo, é possível gerenciar os registros dos clientes (Donos) e dos animais (Pets), criando um vínculo entre eles para controle de atendimentos e agenda.

🗂 Models Criados
O sistema conta com os seguintes modelos principais no banco de dados:

Dono: Responsável por armazenar as informações dos clientes (ex: nome, contato).

Pet: Responsável por armazenar os dados dos animais (ex: nome, raça), vinculado a um Dono.

🛠 Tecnologias Usadas
Python 3: Linguagem de programação principal.

Django: Framework web utilizado para o desenvolvimento do backend e interface administrativa.

SQLite: Banco de dados relacional (padrão do Django para desenvolvimento).

HTML/CSS: Utilizados na interface do painel administrativo do Django.

🚀 Instruções para Rodar

executar o comando python manage.py runserver e acessar a URl http://127.0.0.1:8000/admin

Os templates estão criados e adereçados no views.py do modelo Cadastros, mas não estão propriamente estrurados por falta de ajustes.
