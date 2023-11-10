from turtle import title
import streamlit as st

st.set_page_config(
    page_title="Davidson's Core Criteria Digital Instrument",
    page_icon=":chart:",
    # initial_sidebar_state="expanded",
    layout="wide"
)
st.header("Davidson's Core Criteria Digital Instrument")

nome_avaliador = st.text_input('Nome do avaliador')
col1, col2 = st.columns(2)
with col1:
    nome_projeto = st.text_input('Nome do projeto')
with col2:
    data = st.date_input('Data do projeto')

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ['Validade', 'Utilidade', 'Conduta', 'Credibilidade', 'Custos'], 
    )

with tab1:
    with st.expander('Veja a definição de **Validade**'):
        st.write("""
                 Uma meta-avaliação deve sempre verificar até que ponto as conclusões alcançadas pela equipe de avaliação são justificadas. Lembre-se de que as conclusões avaliativas vêm tanto de fatos descritivos (ou seja, dos dados) quanto de valores relevantes. Os valores relevantes podem nos dizer quais critérios incluir, quais critérios são os mais importantes e quão forte um desempenho deve ser considerado satisfatório, bom e/ou excelente. Portanto, em uma meta-avaliação, é importante verificar com muito cuidado as fontes e os usos tanto dos fatos descritivos quanto dos valores relevantes.
                 """)
st.button("Enviar")