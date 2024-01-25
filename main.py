import streamlit as st
import extra_streamlit_components as stx
from st_pages import Page, _hide_pages, show_pages
from streamlit_extras.switch_page_button import switch_page
from enum import Enum


st.set_page_config(
    page_title="Davidson's 5 Core Criteria Digital Instrument",
    page_icon=":five:",
    initial_sidebar_state="collapsed",
    layout="wide",
)
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("relatorio.py", "relatorio", ":books:"),
    ]
)

Grade = Enum("Grade", {"A":5, "B":4, "C":3, "D":2, "E":1})
grade_nameslist = [grade.name for grade in Grade]


st.markdown(
    """<script>document.querySelector('[data-testid="collapsedControl"]').remove()<script>""",
    unsafe_allow_html=True,
)

blank = st.container()

blank.title(
    "Davidson's :red[5] Core Criteria :red[(Meta-)]Evaluation Digital Instrument"
)

cm = stx.CookieManager()

with blank.container():
    nome_avaliador = st.text_input("Nome do avaliador")
    col1, col2 = st.columns(2)
    with col1:
        nome_projeto = st.text_input("Nome do projeto")
    with col2:
        data = st.date_input("Data do projeto", format="DD/MM/YYYY")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Validade", "Utilidade", "Conduta", "Credibilidade", "Custos"],
    )

    with tab1:
        st.header("Validade")
        with st.expander(
            "Expandir a definição da categoria (meta-)avaliativa: **Validade**"
        ):
            st.write(
                """
              Uma meta-avaliação deve sempre verificar até que ponto as conclusões alcançadas pela equipe de avaliação são justificadas. Lembre-se de que as conclusões avaliativas vêm tanto de fatos descritivos (ou seja, dos dados) quanto de valores relevantes. Os valores relevantes podem nos dizer quais critérios incluir, quais critérios são os mais importantes e quão forte um desempenho deve ser considerado satisfatório, bom e/ou excelente. Portanto, em uma meta-avaliação, é importante verificar com muito cuidado as fontes e os usos tanto dos fatos descritivos quanto dos valores relevantes.

              Identifica fontes de dados, justificativas, julgamentos e valores atribuídos, esclarecendo todas as associações.
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

    with tab2:
        st.header("Utilidade")
        with st.expander(
            "Expandir a definição da categoria (meta-)avaliativa: **Utilidade**"
        ):
            st.write(
                """
              Associa o valor relacionado pelos stakeholders à avaliação e aos seus resultados, possibilitando respostas relevantes para questões pertinentes e tomadas de decisão, relativas ao meta-avaliando.
              """
            )
            st.write(
                "Relevância da avaliação e dos achados para as questões ou decisões dos interessados; Disponibilidade oportuna da avaliação e dos achados para os envolvidos e interessados; Comunicação da avaliação e dos achados em linguagem(ns) e mídia(s) apropriadas."
            )
    with tab3:
        st.header("Conduta")
        with st.expander(
            "Expandir a definição da categoria (meta-)avaliativa: **Conduta**"
        ):
            st.write(
                """
              Diz respeito procedimento avaliativo participativo e não invasivo, observando respeito aos stakeholders e a padrões pertinentes - legais, éticos, profissionais, de adequação cultural, dentre outros.
              """
            )
        st.write(
            "Conformidade com legislações e/ou normas pertinentes (local, nacional e internacional); Respeito aos padrões éticos e culturais; Abordagem aos envolvidos de forma participativa e não invasiva; Conformidade com padrões profissionais em Avaliação."
        )

    with tab4:
        st.header("Credibilidade")
        with st.expander(
            "Expandir a definição da categoria (meta-)avaliativa: **Credibilidade**"
        ):
            st.write(
                """
                  Relativo à recepção da avaliação e dos seus resultados pelos stakeholders, considerando a responsabilização e possíveis repercussões.
                  """
            )
        st.write(
            "Evidência de familiaridade com o contexto; Indícios de independência, imparcialidade e/ou ausência de conflitos de interesses; Domínio dos conhecimentos em Avaliação e no conteúdo apreciado."
        )
    with tab5:
        st.header("Custos")

        with st.expander(
            "Expandir a definição da categoria (meta-)avaliativa: **Custos**"
        ):
            st.write(
                """
              Referem-se a dispêndios na (meta-)avaliação, podendo ser constituídos de esforços empenhados, tempo gasto, além de recursos financeiros.
              """
            )
            st.write(
                "Especificação dos tipos de custos envolvidos; Explicitação da relação custo-benefício do processo avaliativo."
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


col_btn_1, col_btn_2 = st.columns([1, 12])
if col_btn_1.button(
    "Enviar", type="primary", help="Envia os dados e segue para o relatório"
):
    switch_page("relatorio")

    # cookie_manager.set("nome_avaliador", nome_avaliador)
    # st.write(cookie_manager.get_all())

if col_btn_2.button("Reiniciar", help="Recomeça a avaliação, limpando todos os campos"):
    st.rerun()
