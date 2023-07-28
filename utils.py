from pymongo import MongoClient
import streamlit as st

class Utils:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def mongodb_con():
        """Returns the worldsbk db in mongo"""
        client = MongoClient(st.secrets["mongodb_connection"])
        worldsbk_db = client.worldsbk

        return worldsbk_db