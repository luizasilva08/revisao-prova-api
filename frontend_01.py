import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌦️",
    layout="wide",
)

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Estação meteorológica — Jaraguá do Sul/SC")
st.divider()

if st.button("🔄 Atualizar dados"):
    st.rerun()

try:
    with st.spinner("Consultando a API meteorológica..."):
        dados = obter_dados_meteorologicos()
        st.success(f"Dados meteorológicos carregados. (Leitura: {dados['current']['time']})")

        st.subheader("Condições atuais")

        col1, col2, col3 = st.columns(3)
        col1.metric("Temperatura", f"{dados['current']['temperature_2m']} °C")
        col2.metric("Sensação térmica", f"{dados['current']['apparent_temperature']} °C")
        col3.metric("Umidade", f"{dados['current']['relative_humidity_2m']} %")

        col4, col5, _ = st.columns(3)
        col4.metric("Precipitação", f"{dados['current']['precipitation']} mm")
        col5.metric("Velocidade do vento", f"{dados['current']['wind_speed_10m']} km/h")

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
