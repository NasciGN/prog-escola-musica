# Escola de Música

## Sobre a atividade

Este é um projeto de um sistema web desenvolvido em Django e Bootstrap/HTML, criado para gerenciar orquestras, músicos, instrumentos, apresentações, sinfonias e suas respectivas associações.

## Funcionalidades

- Adicionar, visualizar, editar e excluir instrumentos musicais.
- Gerenciar músicos, incluindo a associação com um instrumento específico.
- Registrar e gerenciar apresentações musicais, incluindo a data e o local.
- Criar sinfonias e associá-las a orquestras específicas.
- Gerenciar orquestras, incluindo a adição e remoção de músicos, apresentações e sinfonias.

## Tecnologias Utilizadas

- Django: Framework web em Python para o desenvolvimento do backend.
- Bootstrap/HTML: Utilizados para criar o frontend responsivo e amigável ao usuário.

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

- [ ] Criar o modelo Instrumento.
- [ ] Criar o modelo Musico.
- [ ] Criar o modelo Apresentacao.
- [ ] Criar o modelo Sinfonia.
- [ ] Criar o modelo Orquestra.

#### Instrumentos

- [ ] Implementar views para adicionar, visualizar, editar e excluir instrumentos.
- [ ] Configurar as URLs correspondentes para as views de instrumentos.

#### Músicos

- [ ] Implementar views para adicionar, visualizar, editar e excluir músicos.
- [ ] Configurar as URLs correspondentes para as views de músicos.

#### Apresentações

- [ ] Implementar views para adicionar, visualizar, editar e excluir apresentações.
- [ ] Configurar as URLs correspondentes para as views de apresentações.

#### Sinfonias

- [ ] Implementar views para adicionar, visualizar, editar e excluir sinfonias.
- [ ] Configurar as URLs correspondentes para as views de sinfonias.

#### Orquestras

- [ ] Implementar views para adicionar, visualizar, editar e excluir orquestras.
- [ ] Configurar as URLs correspondentes para as views de orquestras.

## Contribuição

Se você deseja contribuir para o projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Implemente as alterações.
4. Faça o commit das suas alterações (`git commit -m 'Adiciona uma nova feature'`).
5. Faça o push para a branch (`git push origin feature/nome-da-feature`).
6. Abra um Pull Request.
