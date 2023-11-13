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

                 Identifica fontes de dados, justificativas, julgamentos e valores atribuídos, esclarecendo todas as associações.
                 """)
    st.write("Cobertura das fontes relevantes de valor; Cobertura ampla do processo, do(s) resultado(s) e custo(s); Não inclusão de critérios irrelevantes ou ilícitos; Incorporação dos dados que remetem diretamente ao critério; Realização de análises apropriadas aos dados; Explicitação dos procedimentos adotados na interpretação dos dados; Explicitação da procedência das conclusões avaliativas; Inclusão de recomendações justificáveis, realizáveis e eficazes.")
with tab2:
    with st.expander('Veja a definição de **Validade**'):
        st.write("""
                 Associa o valor relacionado pelos stakeholders à avaliação e aos seus resultados, possibilitando respostas relevantes para questões pertinentes e tomadas de decisão, relativas ao meta-avaliando.

                 """)
    st.write("Relevância da avaliação e dos achados para as questões ou decisões dos interessados; Disponibilidade oportuna da avaliação e dos achados para os envolvidos e interessados; Comunicação da avaliação e dos achados em linguagem(ns) e mídia(s) apropriadas.")
with tab3:
    with st.expander('Veja a definição de **Conduta**'):
        st.write("""
                 Diz respeito procedimento avaliativo participativo e não invasivo, observando respeito aos stakeholders e a padrões pertinentes - legais, éticos, profissionais, de adequação cultural, dentre outros.

                 """)
    st.write("Conformidade com legislações e/ou normas pertinentes (local, nacional e internacional); Respeito aos padrões éticos e culturais; Abordagem aos envolvidos de forma participativa e não invasiva; Conformidade com padrões profissionais em Avaliação.")
    
with tab4:
    with st.expander('Veja a definição de **Credibilidade**'):
        st.write("""
                 Relativo à recepção da avaliação e dos seus resultados pelos stakeholders, considerando a responsabilização e possíveis repercussões.
                 """)
    st.write("Evidência de familiaridade com o contexto; Indícios de independência, imparcialidade e/ou ausência de conflitos de interesses; Domínio dos conhecimentos em Avaliação e no conteúdo apreciado.")
with tab5:
    st.header("Custos")
    with st.expander('Veja a definição de **Custos**'):
        st.write("""
                 Referem-se a dispêndios na (meta-)avaliação, podendo ser constituídos de esforços empenhados, tempo gasto, além de recursos financeiros.
                 """)
        st.write("Especificação dos tipos de custos envolvidos; Explicitação da relação custo-benefício do processo avaliativo.")
    check = st.checkbox("Desabilitar")
    option1 = st.selectbox("Especificação dos tipos de custos envolvidos",
                          ("A", "B", "C", "D", "E"),
                          index=None,
                          placeholder="Selecione a sua nota")
    area = st.text_area("Justificativa")
    option2 = st.selectbox("Explicitação da relação custo-benefício do processo avaliativo",
                          ("A", "B", "C", "D", "E"),
                          index=None,
                          placeholder="Selecione a sua nota")
    area2 = st.text_area("Justificativa", key="area2")
st.button("Enviar")