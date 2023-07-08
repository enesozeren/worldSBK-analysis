import http.client
import json
import pandas as pd
from dotenv import load_dotenv
import os
import time

class DataAnalysis:
    def __init__(self) -> None:
        load_dotenv()
        self.key=os.getenv('api_key')
        self.conn = http.client.HTTPSConnection("api.sportradar.com")

    def competitors_standings(self) -> pd.DataFrame:
        season_id = self.get_season_id("Superbike", "2023")
        worldsbk_2023_stage_data = self.api_call(f"/motogp/trial/v2/en/sport_events/{season_id}/summary.json?api_key={self.key}")
        worldsbk_2023_competitors_json = worldsbk_2023_stage_data['stage']['competitors']
        worldsbk_2023_competitors_df = pd.json_normalize(worldsbk_2023_competitors_json)
        return worldsbk_2023_competitors_df

    def get_season_id(self, tournament, year) -> str:
        season_data = self.api_call(f"/motogp/trial/v2/en/seasons.json?api_key={self.key}")
        season_data = pd.json_normalize(season_data['stages'])
        return list(season_data[season_data['description']==f"{tournament} {year}"]["id"])[0]
    
    def api_call(self, url) -> json.loads:
        self.conn.request("GET", url)
        res = self.conn.getresponse()
        data = res.read()
        data = json.loads(data)
        time.sleep(1.1)
        return data
        


