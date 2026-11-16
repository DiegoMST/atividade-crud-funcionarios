# Roteiro para o vídeo da Atividade Avaliativa 2

**Duração sugerida:** de 5 a 7 minutos. Use suas próprias palavras. Se houver dupla, ambos devem aparecer e explicar o código e as telas.

## 1. Apresentação (30 segundos)
Fale seu nome, dos integrantes e explique que o projeto é um CRUD de funcionários feito em Python com Django, Bootstrap e MySQL.

## 2. Mostrar o código (1 a 2 minutos)
- `app/models.py`: mostre os campos `nome`, `cpf`, `email` e `remuneracao`.
- `app/views.py`: mostre `CreateView`, `ListView`, `UpdateView`, `DetailView` e `DeleteView`.
- `app/urls.py`: mostre como cada rota chama uma view.
- `funcionario/settings.py`: indique o uso de `django.db.backends.mysql`.
- `app/templates/`: explique os formulários, a tabela de listagem e o botão de exclusão com confirmação.

## 3. Demonstração do CRUD (2 minutos)
1. Faça um cadastro com **dados fictícios**.
2. Abra a listagem e a página de detalhes.
3. Edite a remuneração e salve.
4. Exclua o funcionário e confirme a exclusão.

## 4. Persistência no MySQL (1 minuto)
Para ficar clara, faça a sequência **cadastro → consulta ao MySQL → edição → nova consulta → exclusão → última consulta**.
No Windows, execute `CONSULTAR-BANCO.bat` em cada etapa e mostre a quantidade e os registros da tabela `app_funcionario`.

## 5. GitHub (30 segundos)
Abra o repositório público e mostre `README.md`, `app/`, `funcionario/`, `Dockerfile` e `compose.yaml`.

## 6. Encerramento (15 segundos)
Explique que os registros ficam no MySQL e que o Docker usa volume persistente para manter os dados.

## Conferência final
- O áudio está compreensível, o código e a consulta SQL podem ser lidos e todos os integrantes aparecem.
- O vídeo no YouTube está **Público** ou **Não listado**, nunca Privado.
- Os links do repositório e do vídeo estão acessíveis sem uma conta especial.
