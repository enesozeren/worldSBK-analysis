import streamlit as st
from pageobjects.standingspage import StandingsPage
from pageobjects.mainpage import MainPage
from pageobjects.predictionspage import PredictionsPage

class App:
    def __init__(self) -> None:
        st.set_page_config(page_title='WorldSBK Analysis')

    def create_mainpage(self) -> None:
        self.mainpage_obj = MainPage()
        self.mainpage_obj.introduction()

    def create_standings(self) -> None:
        self.standingspage_obj = StandingsPage()
        self.standingspage_obj.competitor_dashboards()

    def create_predictions(self) -> None:
        self.predictionspage_obj = PredictionsPage()