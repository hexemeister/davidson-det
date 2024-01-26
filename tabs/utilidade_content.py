import streamlit as st
from utils.enums import grade_nameslist

def utilidade_content():
    st.header("Utilidade")
    with st.expander(
        "Expandir a definição da categoria (meta-)avaliativa: **Utilidade**"
    ):
        st.markdown(
            """
            Associa o valor relacionado pelos stakeholders à avaliação e aos seus resultados, possibilitando respostas relevantes para questões pertinentes e tomadas de decisão, relativas ao meta-avaliando.
            
            Indicadores considerados:
            1. Relevância da avaliação e dos achados para as questões ou decisões dos interessados
            2. Disponibilidade oportuna da avaliação e dos achados para os envolvidos e interessados
            3. Comunicação da avaliação e dos achados em linguagem(ns) e mídia(s) apropriadas.
            """
        )
    with st.expander("Recolher item", expanded=True):
        util_op_1 = st.selectbox(
            "Relevância da avaliação e dos achados para as questões ou decisões dos interessados",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="util_op_1"
        )
        util_why_1 = st.text_area("Justificativa", key="util_why_1")
    with st.expander("Recolher item", expanded=True):
        util_op_2 = st.selectbox(
            "Disponibilidade oportuna da avaliação e dos achados para os envolvidos e interessados",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="util_op_2"
        )
        util_why_2 = st.text_area("Justificativa", key="util_why_2")
    with st.expander("Recolher item", expanded=True):
        util_op_3 = st.selectbox(
            "Comunicação da avaliação e dos achados em linguagem(ns) e mídia(s) apropriadas.",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="util_op_3"
        )
        util_why_3 = st.text_area("Justificativa", key="util_why_3")
