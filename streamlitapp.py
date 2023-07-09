import streamlit as st
from standings import Standings

class App:
    def __init__(self) -> None:
        st.set_page_config(page_title='WorldSBK Analysis')

    def create_mainpage(self) -> None:
        st.header("What is this page about?")

    def create_standings(self) -> None:
        self.standings_obj = Standings()
        self.standings_obj.competitor_dashboards()

    def create_predictions(self) -> None:
        st.header("TBD")

    def create_analysis(self) -> None:
        st.header("TBD")