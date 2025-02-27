# Calculadora API

API RESTful para operações matemáticas básicas usando Python e Flask.

## Requisitos Iniciais
Antes de prosseguir, certifique-se de ter o Python instalado (versão 3.8 ou superior recomendada). Se não tiver, instale-o:
- **Linux/macOS**: `sudo apt update && sudo apt install python3 python3-venv` (Ubuntu/Debian) ou equivalente.
- **Windows**: Baixe e instale em [python.org](https://www.python.org/downloads/).
Verifique com `python3 --version` ou `python --version`. Em seguida, siga os passos abaixo.

## Instruções de Execução
1. Clone o repositório: `git clone <URL>`
2. Entre no diretório: `cd calculadora-api`
3. Ative o ambiente virtual: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute o projeto: `python -m src.main.python.com.example.calculadora.controller.app` (use este comando em vez de executar o arquivo diretamente)
6. Acesse a API em: `http://localhost:5000/calculations`

## Observações Importantes
- **Execução como Módulo**: O comando `python -m` é necessário devido à estrutura de pacotes. Executar `python src/main/python/com/example/calculadora/controller/app.py` diretamente pode causar erros de importação.
- **PYTHONPATH para Testes**: Para executar os testes, use `PYTHONPATH=. pytest src/test/` para garantir que o diretório `src` seja reconhecido.

## Execução das Funcionalidades
Após iniciar a API, você pode testar os endpoints usando ferramentas como `curl`, Postman ou qualquer cliente HTTP. Exemplos:
- **Somar um vetor**:
  - Comando: `curl -X POST -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}' http://localhost:5000/calculations/sum`
  - Resposta esperada: `{"result": 15}`
- **Calcular média**:
  - Comando: `curl -X POST -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}' http://localhost:5000/calculations/average`
  - Resposta esperada: `{"result": 3.0}`
- **Erro (vetor inválido)**:
  - Comando: `curl -X POST -H "Content-Type: application/json" -d '{"numbers": []}' http://localhost:5000/calculations/sum`
  - Resposta esperada: `{"error": "Vetor vazio ou contém valores inválidos"}`

## Execução dos Testes
Para verificar se os testes unitários funcionam:
1. Certifique-se de que o ambiente virtual está ativo (`source venv/bin/activate` ou `venv\Scripts\activate`).
2. Execute o comando: `PYTHONPATH=. pytest src/test/`
3. Os testes validarão as funções `sum_numbers` e `average_numbers` da classe `Numbers`. Resultados bem-sucedidos mostrarão "OK" para cada teste.

## Endpoints
- `POST /calculations/sum` - Soma um vetor de inteiros
  - Exemplo de requisição:
    ```json
    {"numbers": [1, 2, 3, 4, 5]}