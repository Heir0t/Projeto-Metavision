# Metavision

Este projeto é uma API desenvolvida em FastAPI que permite a detecção de beacons Bluetooth Low Energy (BLE) e a emissão de alertas quando um usuário se aproxima de um beacon. A API utiliza dados configurados previamente no arquivo `beacons.json` e retorna mensagens associadas a cada beacon identificado pelo seu endereço MAC.

---

## Bibliotecas Requeridas

As seguintes bibliotecas são utilizadas no projeto:

- `fastapi`: Framework web para criação da API.
- `uvicorn[standard]`: Servidor ASGI que roda a API FastAPI.
- `pydantic`: Validação e modelagem de dados.
- `requests`: Para realizar requisições HTTP de simulação.
- `bleak`: Scanner Bluetooth BLE multiplataforma (não utilizado diretamente neste momento, mas essencial para a detecção de beacons em um sistema real).

---

## Instalação

1. Clone ou acesse o diretório do projeto.

2. Instale as dependências no terminal com o seguinte comando:

pip install -r requirements.txt
