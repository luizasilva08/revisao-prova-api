# Revisão para a Prova de API

Projeto da prova prática. Ele pega os dados do tempo de uma API que roda no meu computador (offline) e mostra numa página feita com Streamlit.

Cidade usada: Jaraguá do Sul – SC (latitude -26.4851, longitude -49.0713).

## Arquivos

- `consumidor_api.py` – faz a requisição na API e pega os dados
- `frontend_01.py`, `frontend_02.py`, `frontend_03.py` – três versões da tela
- `requirements.txt` – bibliotecas usadas

## Como instalar

1. Baixar o projeto:

```bash
git clone https://github.com/luizasilva08/revisao-prova-api.git
cd revisao-prova-api
```

2. Instalar as bibliotecas (principais: `streamlit`, `requests` e `uvicorn`):

```bash
pip install -r requirements.txt
```

## Como rodar

1. Baixar a API do professor: https://github.com/jpsvalentim/api-meteorologica-offline
2. Em um terminal, dentro da pasta da API, ligar ela (o terminal tem que ficar aberto):

```bash
uvicorn app.main:app --reload
```

A API fica em http://127.0.0.1:8000 e a documentação em http://127.0.0.1:8000/docs

3. Em **outro terminal**, na pasta deste projeto, rodar uma das telas:

```bash
streamlit run frontend_01.py
```

(ou `frontend_02.py` / `frontend_03.py`)

## Sobre a API

- Endereço usado: `GET http://127.0.0.1:8000/v1/forecast`
- Parâmetros utilizados: `parametros = {
    "latitude": -26.4851,
    "longitude": -49.0713
}`

- Retorna em JSON: temperatura (`temperature_2m`), umidade (`relative_humidity_2m`), sensação térmica (`apparent_temperature`), precipitação (`precipitation`) e vento (`wind_speed_10m`), dentro de `current`.
- Os nomes têm que ser escritos exatamente assim.
- Códigos: 200 deu certo, 400 parâmetro inválido, 404 não encontrado, 500 erro interno.

## Se der erro

- Erro de conexão: a API não está ligada. Conferir se o terminal do `uvicorn` está aberto.
