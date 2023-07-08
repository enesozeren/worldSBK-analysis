import streamlit as st
from analysis import DataAnalysis

class App:
    def __init__(self) -> None:
        st.set_page_config(page_title='WorldSBK Analysis')
        st.header('WorldSBK Analysis')
        self.data_analysis_obj = DataAnalysis()

    def create_dashboards(self) -> None:
        self.competitor_dashboards()

    def competitor_dashboards(self) -> None:
        competitor_standings_df = self.data_analysis_obj.competitors_standings()
        st.dataframe(
            competitor_standings_df[["name", "team.name", "result.points"]],
            column_config={
                "name": "Rider",
                "team.name": "Team",
                "result.points": "Points",
                "result.points": st.column_config.NumberColumn(
                    "Points",
                    format="%d 🛵",
                ), 
            },
            hide_index=True,
        )