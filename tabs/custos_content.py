import streamlit as st
from utils.enums import grade_nameslist


def custos_content():
    st.header("Custos")

    with st.expander("Expandir a definição da categoria (meta-)avaliativa: **Custos**"):
        st.markdown(
            """
            Referem-se a dispêndios na (meta-)avaliação, podendo ser constituídos de esforços empenhados, tempo gasto, além de recursos financeiros.
            
            Indicadores considerados:
            1. Especificação dos tipos de custos envolvidos; 
            2. Explicitação da relação custo-benefício do processo avaliativo."""
        )
    no_costs = st.toggle("Desabilitar (meta-)avaliação de Custos", value=True)
    if no_costs:
        with st.expander("Recolher seção", expanded=True):
            option1 = st.selectbox(
                "Especificação dos tipos de custos envolvidos",
                grade_nameslist,
                index=None,
                placeholder="Selecione a sua nota",
            )
            why1 = st.text_area("Justificativa", key="cus_op_1")
        with st.expander("Recolher seção", expanded=True):
            option2 = st.selectbox(
                "Explicitação da relação custo-benefício do processo avaliativo",
                grade_nameslist,
                index=None,
                placeholder="Selecione a sua nota",
            )
            why2 = st.text_area("Justificativa", key="cus_why_2")
    else:
        no_costs_why = st.text_area(
            "Por que não avaliar a categoria Custos?", key="no_costs_why"
        )
