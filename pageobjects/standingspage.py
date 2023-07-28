import pandas as pd
from utils import Utils
import streamlit as st

class StandingsPage:
    def __init__(self) -> None:
        st.header("Summary Table")

    def competitor_dashboards(self) -> None:
        competitor_standings_df = self.competitors_standings()
        st.dataframe(
            competitor_standings_df[["name", "team.name", "result.points", "result.victories", \
                                     "result.podiums", "result.pole_positions"]],
            column_config={
                "name": "Rider",
                "team.name": "Team",
                "result.points": st.column_config.NumberColumn(
                    "Points",
                    format="%d 🛵",
                ), 
                "result.victories": st.column_config.NumberColumn(
                    "Wins",
                    format="%d 🏆",
                ),                 
                "result.podiums": "Podiums",
                "result.pole_positions": "Pole"
            },
            hide_index=True,
        )

    def competitors_standings(self) -> pd.DataFrame:
        worldsbk_db = Utils.mongodb_con()
        data = worldsbk_db.standings.find({})
        data = data[0]["stage"]["competitors"]
        worldsbk_2023_competitors_df = pd.json_normalize(data)
        return worldsbk_2023_competitors_df