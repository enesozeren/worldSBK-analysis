import pandas as pd
from utils import Utils
import streamlit as st

class Standings:
    def __init__(self) -> None:
        pass

    def competitor_dashboards(self) -> None:
        competitor_standings_df = self.competitors_standings()
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

    def competitors_standings(self) -> pd.DataFrame:
        season_id = self.get_season_id("Superbike", "2023")
        worldsbk_2023_stage_data = Utils.api_call(f"/motogp/trial/v2/en/sport_events/{season_id}/summary.json")
        worldsbk_2023_competitors_json = worldsbk_2023_stage_data['stage']['competitors']
        worldsbk_2023_competitors_df = pd.json_normalize(worldsbk_2023_competitors_json)
        return worldsbk_2023_competitors_df

    def get_season_id(self, tournament, year) -> str:
        season_data = Utils.api_call(f"/motogp/trial/v2/en/seasons.json")
        season_data = pd.json_normalize(season_data['stages'])
        return list(season_data[season_data['description']==f"{tournament} {year}"]["id"])[0]