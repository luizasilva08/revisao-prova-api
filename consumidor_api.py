import requests

def obter_dados_meteorologicos():
    url = "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude":"-26.4851",
        "longitude":"-49.0713",
    }

    resposta = requests.get(url, params = parametros, timeout=15)

    if resposta.status_code == 200:
        print(f"Código da requisição: {resposta.status_code}")
        print(f"Erros na requisição: {resposta.raise_for_status()}")
        dados = resposta.json()

        umidade = dados["current"]["relative_humidity_2m"]
        temperatura = dados["current"]["temperature_2m"]
        sensacao = dados["current"]["apparent_temperature"]
        precipitacao = dados["current"]["precipitation"]
        vento = dados["current"]["wind_speed_10m"]

        print(f"Temperatura: {temperatura} °C")
        print(f"Umidade: {umidade} %")
        print(f"Sensação térmica: {sensacao}")
        print(f"Precipitação: {precipitacao}")
        print(f"Velocidade do vento: {vento} ")
        return dados

    else:
        print("Requisição não feita.")

obter_dados_meteorologicos()