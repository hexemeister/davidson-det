import streamlit as st
from utils.enums import grade_nameslist


def conduta_content():
    st.header("Conduta")
    with st.expander(
        "Expandir a definição da categoria (meta-)avaliativa: **Conduta**"
    ):
        st.markdown(
            """
            Diz respeito procedimento avaliativo participativo e não invasivo, observando respeito aos stakeholders e a padrões pertinentes - legais, éticos, profissionais, de adequação cultural, dentre outros.
            
            Indicadores considerados:
            1. Conformidade com legislações e/ou normas pertinentes (local, nacional e internacional)
            2. Respeito aos padrões éticos e culturais
            3. Abordagem aos envolvidos de forma participativa e não invasiva
            4. Abordagem aos envolvidos de forma participativa e não invasiva
            5. Conformidade com padrões profissionais em Avaliação.
            """
        )
    with st.expander("Recolher item", expanded=True):
        cond_op_1 = st.selectbox(
            "Conformidade com legislações e/ou normas pertinentes (local, nacional e internacional)",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cond_op_1",
        )
        cond_why_1 = st.text_area("Justificativa", key="cond_why_1")
    with st.expander("Recolher item", expanded=True):
        cond_op_2 = st.selectbox(
            "Respeito aos padrões éticos e culturais",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cond_op_2",
        )
        cond_why_2 = st.text_area("Justificativa", key="cond_why_2")
    with st.expander("Recolher item", expanded=True):
        cond_op_3 = st.selectbox(
            "Abordagem aos envolvidos de forma participativa e não invasiva",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cond_op_3",
        )
        cond_why_3 = st.text_area("Justificativa", key="cond_why_3")
    with st.expander("Recolher item", expanded=True):
        cond_op_4 = st.selectbox(
            "Abordagem aos envolvidos de forma participativa e não invasiva",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cond_op_4",
        )
        cond_why_4 = st.text_area("Justificativa", key="cond_why_4")
    with st.expander("Recolher item", expanded=True):
        cond_op_5 = st.selectbox(
            "Conformidade com padrões profissionais em Avaliação.",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="cond_op_5",
        )
        cond_why_5 = st.text_area("Justificativa", key="cond_why_5")
