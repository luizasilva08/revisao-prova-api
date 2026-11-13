import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Estação Meteorológica",
    page_icon="🌡️",
    layout="centered",
)

st.title("🌡️ Estação Meteorológica")
st.write("Monitoramento das condições ambientais")
st.caption("Jaraguá do Sul — Santa Catarina")
st.divider()

try:
    with st.spinner("Obtendo informações meteorológicas..."):
        dados = obter_dados_meteorologicos()

    st.success("Consulta realizada com sucesso!")

    st.subheader("🌡️ Temperatura")
    col1, col2 = st.columns(2)
    col1.metric(
        "Temperatura do ar",
        f"{dados['current']['temperature_2m']} °C",
    )
    col2.metric(
        "Sensação térmica",
        f"{dados['current']['apparent_temperature']} °C",
    )

    st.divider()

    st.subheader("💨 Condições Atmosféricas")
    col3, col4, col5 = st.columns(3)
    col3.metric(
        "Umidade relativa",
        f"{dados['current']['relative_humidity_2m']} %",
    )
    col4.metric(
        "Precipitação",
        f"{dados['current']['precipitation']} mm",
    )
    col5.metric(
        "Velocidade do vento",
        f"{dados['current']['wind_speed_10m']} km/h",
    )

    st.caption(f"Última atualização: {dados['current']['time']}")

except Exception as e:
    st.error(f"Erro ao obter informações meteorológicas: {e}")
