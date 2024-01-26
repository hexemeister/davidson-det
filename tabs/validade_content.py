import streamlit as st
from utils.enums import grade_nameslist

def validade_content():
    st.header("Validade")
    with st.expander(
        "Expandir a definição da categoria (meta-)avaliativa: **Validade**"
    ):
        st.markdown(
            """
            Uma meta-avaliação deve sempre verificar até que ponto as conclusões alcançadas pela equipe de avaliação são justificadas. Lembre-se de que as conclusões avaliativas vêm tanto de fatos descritivos (ou seja, dos dados) quanto de valores relevantes. Os valores relevantes podem nos dizer quais critérios incluir, quais critérios são os mais importantes e quão forte um desempenho deve ser considerado satisfatório, bom e/ou excelente. Portanto, em uma meta-avaliação, é importante verificar com muito cuidado as fontes e os usos tanto dos fatos descritivos quanto dos valores relevantes.

            Identifica fontes de dados, justificativas, julgamentos e valores atribuídos, esclarecendo todas as associações.
            
            Indicadores considerados:
            1. Cobertura das fontes relevantes de valor
            2. Cobertura ampla do processo, do(s) resultado(s) e custo(s)
            3. Não inclusão de critérios irrelevantes ou ilícitos
            4. Incorporação dos dados que remetem diretamente ao critério
            5. Realização de análises apropriadas aos dados
            6. Explicitação dos procedimentos adotados na interpretação dos dados
            7. Explicitação da procedência das conclusões avaliativas
            8. Inclusão de recomendações justificáveis, realizáveis e eficazes.
            """
        )
    with st.expander("Recolher item", expanded=True):
        val_op_1 = st.selectbox(
            "Cobertura das fontes relevantes de valor",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_1"
        )
        val_why_1 = st.text_area("Justificativa", key="val_why_1")
    with st.expander("Recolher item", expanded=True):
        val_op_2 = st.selectbox(
            "Cobertura ampla do processo, do(s) resultado(s) e custo(s)",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_2"
        )
        val_why_2 = st.text_area("Justificativa", key="val_why_2")
    with st.expander("Recolher item", expanded=True):
        val_op_3 = st.selectbox(
            "Não inclusão de critérios irrelevantes ou ilícitos",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_3"
        )
        val_why_3 = st.text_area("Justificativa", key="val_why_3")
    with st.expander("Recolher item", expanded=True):
        val_op_4 = st.selectbox(
            "Incorporação dos dados que remetem diretamente ao critério",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_4"
        )
        val_why_4 = st.text_area("Justificativa", key="val_why_4")
    with st.expander("Recolher item", expanded=True):
        val_op_5 = st.selectbox(
            "Realização de análises apropriadas aos dados",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_5"
        )
        val_why_5 = st.text_area("Justificativa", key="val_why_5")
    with st.expander("Recolher item", expanded=True):
        val_op_6 = st.selectbox(
            "Explicitação dos procedimentos adotados na interpretação dos dados",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_6"
        )
        val_why_6 = st.text_area("Justificativa", key="val_why_6")
    with st.expander("Recolher item", expanded=True):
        val_op_7 = st.selectbox(
            "Explicitação da procedência das conclusões avaliativas",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_7"
        )
        val_why_7 = st.text_area("Justificativa", key="val_why_7")
    with st.expander("Recolher item", expanded=True):
        val_op_8 = st.selectbox(
            "Inclusão de recomendações justificáveis, realizáveis e eficazes.",
            grade_nameslist,
            index=None,
            placeholder="Selecione a sua nota",
            key="val_op_8"
        )
        val_why_8 = st.text_area("Justificativa", key="val_why_8")