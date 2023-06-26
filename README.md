# Escola de Música

## Sobre a atividade

Este é um projeto de um sistema web desenvolvido em Django e Bootstrap/HTML, criado para gerenciar orquestras, músicos, instrumentos, apresentações, sinfonias e suas respectivas associações.

## Funcionalidades

- Adicionar, visualizar, editar e excluir instrumentos musicais.
- Gerenciar músicos, incluindo a associação com um instrumento específico.
- Registrar e gerenciar apresentações musicais, incluindo a data e o local.
- Criar sinfonias e associá-las a orquestras específicas.
- Gerenciar orquestras, incluindo a adição e remoção de músicos, apresentações e sinfonias.

***
## Alunos
- Gabriel Nascimento
- Isaías Felix
- Murilo José
- Thauan Felipe
***
## Tecnologias Utilizadas

- Django: Framework web em Python para o desenvolvimento do backend.
- Bootstrap/HTML: Utilizados para criar o frontend responsivo e amigável ao usuário.

## Permissões

- O sistema foi planejado com algumas permissões específicas para cada usuário.

### Usuário comum

O usuário comum é aquele que cria sua conta pela inteface de login do site. Todo usuário criado pela interface do site por padrão possui as permissões de usuário comum.  

Este usuário tem permissão para realizar o CRUD completo nas seguintes models:

- Apresentação
- Instrumento
- Orquestra

Para as outras duas models (Músicos e Sinfonias), este usuário só tem permissão de visualização.

***

### Usuário com cargo de Professor.

Este usuário está no grupo de professores.  
O grupo de professores tem permissão para realizar o CRUD em todas as models do projeto, porém não tem permissão para acessar o painel de administração do site.  
Para que um usuário faça parte do grupo de professores é necessário que um administrador, através do painel de administração do site, atribua o grupo de professores para esse usuário.  
Somente um administrador pode realizar tal modificação.

***

### Administrador

Um administrador tem acesso total as funcionalidades do site.  
Ao logar pela interface do site, um novo campo no menu de navegação é exibido com o nome de 'Administração'.  
Ele dá acesso ao painel de administração do Django. É lá que alterações de permissões, como a de colocar um usuário no grupo de professores, serão feitas.  
Somente um administrador, nativamente, tem a permissão de acesso dessa página, e somente ele pode adicionar outros administradores.

***

## Configuração do Ambiente

- [x] Instalar o Python.
- [x] Instalar o Django.
- [x] Configurar o ambiente virtual.

## Iniciando o Servidor de Desenvolvimento

Para iniciar o servidor de desenvolvimento do Django, execute o seguinte comando no terminal:

`python manage.py runserver`

Acesse o sistema através do URL [http://localhost:8000/](http://localhost:8000/).

## Requisitos

Os requisitos do projeto estão listados no arquivo `requirements.txt`. Para instalar as dependências, utilize o seguinte comando:

`pip install -r requirements.txt`

## Desenvolvimento - Atividades a serem realizadas

### Models

- [x] Criar o modelo Instrumento.
- [x] Criar o modelo Musico.
- [x] Criar o modelo Apresentacao.
- [x] Criar o modelo Sinfonia.
- [x] Criar o modelo Orquestra.

#### Instrumentos

- [x] Implementar views para adicionar, visualizar, editar e excluir instrumentos.
- [x] Configurar as URLs correspondentes para as views de instrumentos.

#### Músicos

- [x] Implementar views para adicionar, visualizar, editar e excluir músicos.
- [x] Configurar as URLs correspondentes para as views de músicos.

#### Apresentações

- [x] Implementar views para adicionar, visualizar, editar e excluir apresentações.
- [x] Configurar as URLs correspondentes para as views de apresentações.

#### Sinfonias

- [x] Implementar views para adicionar, visualizar, editar e excluir sinfonias.
- [x] Configurar as URLs correspondentes para as views de sinfonias.

#### Orquestras

- [x] Implementar views para adicionar, visualizar, editar e excluir orquestras.
- [x] Configurar as URLs correspondentes para as views de orquestras.

## Contribuição

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Implemente as alterações.
4. Faça o commit das suas alterações (`git commit -m 'Adiciona uma nova feature'`).
5. Faça o push para a branch (`git push origin feature/nome-da-feature`).
6. Abra um Pull Request.
