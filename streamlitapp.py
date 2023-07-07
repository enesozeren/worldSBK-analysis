import streamlit as st
from dotenv import load_dotenv
import os

class App:
    def __init__(self) -> None:
        load_dotenv()
        self.key=os.getenv('api_key')
        st.set_page_config(page_title='WorldSBK Analysis')
        st.header('WorldSBK Analysis')