import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = obter_dados_meteorologicos()

    st.success("Painel atualizado.")
    st.subheader("Indicadores principais")

    col1, col2, col3 = st.columns(3)
    col1.metric(
        "🌡️ Temperatura",
        f"{dados['current']['temperature_2m']:.1f} °C",
    )
    col2.metric(
        "🤔 Sensação Térmica",
        f"{dados['current']['apparent_temperature']:.1f} °C",
    )
    col3.metric(
        "💧 Umidade",
        f"{dados['current']['relative_humidity_2m']} %",
    )

    col4, col5, _ = st.columns(3)
    col4.metric(
        "🌧️ Precipitação",
        f"{dados['current']['precipitation']:.1f} mm",
    )
    col5.metric(
        "💨 Vento",
        f"{dados['current']['wind_speed_10m']:.1f} km/h",
    )

    st.caption(f"Registro da estação: {dados['current']['time']}")

except Exception as e:
    st.error(f"Erro ao atualizar o painel: {e}")
