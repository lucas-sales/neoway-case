# Neoway-case


> Este projeto recebe um arquivo txt, processa os dados e os grava em uma instância postgres.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Modular o projeto
- [x] Adicionar try except
- [x] Melhorar a Query
- [ ] Melhorar a classe de tratamento de dados

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente do `<docker>`
* Você tem uma máquina `<Windows / Linux / Mac>`.
* Você leu `<guia / link / documentação_relacionada_ao_projeto>`.

## 🚀 Instalando Neoway-case

Para instalar o Neoway-case, siga estas etapas:

Baixe/Clone o repositório na sua máquina e em seguida crie um arquivo na pasta raiz chamado <.env>
com as credenciais do banco postgre que deseja acessar.

Após adicionar as credenciais no arquivo <.env>, execute o comando abaixo para montar a imagem Docker:

Linux e macOS:
```
$ docker-compose up -d --build
```

Windows:
```
$ docker-compose up -d --build
```

Obs: Seu prompt de comando deve estar na pasta raiz do projeto para executar este comando

## ☕ Usando Neoway-case

Para usar Neoway-case, siga estas etapas:

Utilize o comando abaixo para acessar a imagem montada:

Linux e macOS:
```
$ docker exec -it neoway_app bash
```

Windows:
```
$ docker exec -it neoway_app bash
```

Quando o prompt acessar o container basta apenas executar o script principal.

Linux e macOS:
```
/neoway# python main.py
```

Windows:
```
/neoway# python main.py
```
Obs: Nesta versão, o projeto leva em torno de 4:40min para armazenar por volta de 35mil registros.
Para verificar o banco de dados basta usar uma ferramenta como o DBeaver ou o pgAdmin4, se conectar com as credenciais e executar querys.


[⬆ Voltar ao topo](#Neoway-case)<br>
