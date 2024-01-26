import streamlit as st
import extra_streamlit_components as stx
from st_pages import Page,_hide_pages, show_pages
from streamlit_extras.switch_page_button import switch_page


from tabs.validade_content import validade_content
from tabs.utilidade_content import utilidade_content
from tabs.conduta_content import conduta_content
from tabs.credibilidade_content import credibilidade_content
from tabs.custos_content import custos_content
from utils.enums import grade_nameslist

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
        validade_content()

    with tab2:
        utilidade_content()
        
    with tab3:
        conduta_content()

    with tab4:
        credibilidade_content()
        
    with tab5:
        custos_content()


col_btn_1, col_btn_2 = st.columns([1, 12])
if col_btn_1.button(
    "Enviar", type="primary", help="Envia os dados e segue para o relatório"
):
    switch_page("relatorio")

    # cookie_manager.set("nome_avaliador", nome_avaliador)
    # st.write(cookie_manager.get_all())

if col_btn_2.button("Reiniciar", help="Recomeça a avaliação, limpando todos os campos"):
    st.rerun()
