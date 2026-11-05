# Lista de tarefas

Meu primeiro projeto web com Python e Flask.

## Funcionalidades

- Adicionar tarefas.
- Listar tarefas.
- Marcar tarefas como concluídas.
- Excluir tarefas.
- Salvar os dados em um arquivo JSON.

## Como executar no Windows

É necessário ter Python instalado.

1. Crie o ambiente virtual:

   ```powershell
   py -m venv .venv
   ```

2. Instale as dependências:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Inicie o aplicativo:

   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```

4. Acesse http://127.0.0.1:5000 no navegador.

As tarefas são salvas localmente em tarefas.json.
Esse arquivo é criado quando uma tarefa é adicionada.

O aplicativo usa o servidor de desenvolvimento do Flask para uso local.