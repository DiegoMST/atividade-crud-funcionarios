# CRUD de Funcionários — Atividade Avaliativa 2

Projeto acadêmico em **Python, Django, MySQL e Bootstrap 5**, desenvolvido conforme o roteiro da disciplina.

**Integrante 1:** PREENCHER NOME COMPLETO  
**Integrante 2 (se houver):** PREENCHER NOME COMPLETO OU REMOVER ESTA LINHA

## Funcionalidades

O sistema permite cadastrar, listar, visualizar, editar e excluir funcionários. Cada funcionário possui nome, CPF, e-mail e remuneração. Os registros são gravados no MySQL, na tabela `app_funcionario` do banco `funcionarios`.

## Como executar

É necessário ter o **Docker Desktop** aberto (Docker Compose incluso). No Windows, clique em `INICIAR.bat`, aguarde os dois containers iniciarem e acesse:

**http://127.0.0.1:8000/app/lista_funcionarios**

Pelo terminal, na pasta do projeto:

```powershell
docker compose up -d --build
docker compose ps
```

Na primeira execução, a aplicação aplica automaticamente as migrações do Django. O MySQL utiliza um volume Docker chamado `dados_mysql` (prefixado pelo nome do projeto no Docker), mantendo os cadastros mesmo após reiniciar os serviços.

Para encerrar, use `PARAR.bat` ou `docker compose down`. **Não use `docker compose down -v`**, porque isso remove o volume com os registros.

## Comprovar os registros no banco

1. Cadastre um funcionário fictício pelo sistema.
2. Clique em `CONSULTAR-BANCO.bat`: ele executa consultas SQL na tabela `app_funcionario` do MySQL e mostra a quantidade total e os registros.
3. Edite o registro e execute a consulta outra vez; o valor alterado deve aparecer.
4. Exclua o registro e consulte mais uma vez; o total deve diminuir.

Caso a consulta retorne `total_de_funcionarios = 0`, a tabela está vazia: cadastre um funcionário antes de repetir o teste.

## Verificar o funcionamento

Clique em `VERIFICAR.bat`, ou execute:

```powershell
docker compose exec -T sistema python manage.py check
docker compose exec -T -e TEST_USE_SQLITE=1 sistema python manage.py test app
```

Os testes automatizados utilizam SQLite **somente no ambiente isolado de testes**. Ao usar a aplicação normalmente, a persistência é no MySQL. Para comprovar a persistência na avaliação, utilize `CONSULTAR-BANCO.bat`.

## Estrutura

```text
app/
  models.py                  Modelo Funcionario
  views.py                   Views CRUD
  forms.py                   Formulario de cadastro e edicao
  urls.py                    Rotas da aplicacao
  templates/                 Paginas HTML
  static/app/style.css       Ajustes de estilo
  migrations/                Criacao das tabelas
  tests.py                   Testes automatizados
funcionario/
  settings.py                Configuracoes Django / MySQL
  urls.py                    Rotas principais
compose.yaml                 Servicos Django e MySQL
Dockerfile                   Imagem Python
INICIAR.bat                  Inicializa o projeto
PARAR.bat                    Para os servicos
CONSULTAR-BANCO.bat         Consulta registros direto no MySQL
VERIFICAR.bat                Executa verificacoes e testes
PUBLICAR-GITHUB.bat         Ajuda a publicar no repositorio publico
ROTEIRO-VIDEO.md            Sugestao de roteiro da gravacao
```

## Publicar no GitHub

1. Preencha os nomes dos integrantes no início do README.
2. Crie um repositório **público e vazio** chamado `atividade-crud-funcionarios` no GitHub.
3. No Windows, execute `PUBLICAR-GITHUB.bat` e informe seu usuário GitHub. É necessário ter o Git instalado e estar autenticado.
4. Confira que todos os arquivos de código foram enviados e que o repositório é público.

O vídeo da entrega pode seguir `ROTEIRO-VIDEO.md`. O próprio usuário deve gravar e publicar o vídeo no YouTube como **Público** ou **Não listado**.

## Observações de segurança

- Este projeto usa **credenciais padrão de exemplo**, exclusivamente para testes no computador local. Não use essas credenciais em servidores públicos ou ambientes compartilhados.
- **Não publique** um arquivo `.env` com senhas, dados pessoais verdadeiros nem arquivos de banco de dados.
- O Django é iniciado com `DEBUG=1` e servidor de desenvolvimento; o projeto não é uma implantação de produção.
- O MySQL não expõe a porta 3306 ao computador host: somente o serviço Django na rede Docker acessa o banco.
- Para senhas próprias, configure as variáveis descritas em `compose.yaml` antes da primeira inicialização do volume.
