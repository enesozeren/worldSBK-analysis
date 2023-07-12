import streamlit as st
from PIL import Image
import os

class MainPage:
    def __init__(self) -> None:
        st.header("What is this page about?")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image = Image.open(f"{current_dir}/sbk_logo.png")
        st.image(image, width=300)
    
    def introduction(self) -> None:
        st.write("This is a self developed project of https://github.com/enesozeren")
        st.write("For current standings and analysis of riders, check \"Standings\" tab above.")
        st.write("For next race winner predictions, check \"Predictions\" tab above.")
        st.caption("Our data analysis and predictions are provided for informational purposes only, \
                    and we make no guarantees regarding their accuracy or completeness. Users are advised\
                    to independently verify the information and should not rely solely on our analyses for\
                    decision-making purposes.")
        st.caption("We disclaim any liability for any losses or damages arising from the use or \
                   reliance on our data analysis and predictions, and users are solely responsible\
                    for their own actions and decisions based on the information provided.")