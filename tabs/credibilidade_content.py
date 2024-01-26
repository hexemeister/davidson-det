import streamlit as st
from utils.enums import grade_nameslist


def credibilidade_content():
    st.header("Credibilidade")
    with st.expander(
        "Expandir a definição da categoria (meta-)avaliativa: **Credibilidade**"
    ):
        st.markdown(
            """
            Relativo à recepção da avaliação e dos seus resultados pelos stakeholders, considerando a responsabilização e possíveis repercussões.
            Indicadores considerados:
            1. Evidência de familiaridade com o contexto
            2. Indícios de independência, imparcialidade e/ou ausência de conflitos de interesses
            3. Domínio dos conhecimentos em Avaliação e no conteúdo apreciado.
            """
        )
    with st.expander("Recolher item", expanded=True):
        cred_op_1 = st.selectbox(
            "Evidência de familiaridade com o contexto",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cred_op_1",
        )
        cred_why_1 = st.text_area("Justificativa", key="cred_why_1")
    with st.expander("Recolher item", expanded=True):
        cred_op_2 = st.selectbox(
            "Indícios de independência, imparcialidade e/ou ausência de conflitos de interesses",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cred_op_2",
        )
        cred_why_2 = st.text_area("Justificativa", key="cred_why_2")
    with st.expander("Recolher item", expanded=True):
        cred_op_3 = st.selectbox(
            "Domínio dos conhecimentos em Avaliação e no conteúdo apreciado.",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cred_op_3",
        )
        cred_why_3 = st.text_area("Justificativa", key="cred_why_3")
