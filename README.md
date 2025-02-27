# Calculadora API

API RESTful para operações matemáticas básicas usando Python e Flask.

## Instruções de Execução
1. Clone o repositório: `git clone <URL>`
2. Entre no diretório: `cd calculadora-api`
3. Ative o ambiente virtual: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute o projeto: `python src/main/python/com/example/calculadora/controller/app.py`
6. Acesse a API em: `http://localhost:5000/calculations`

## Endpoints
- `POST /calculations/sum` - Soma um vetor de inteiros
  - Exemplo de requisição:
    ```json
    {"numbers": [1, 2, 3, 4, 5]}# calculadora-api
