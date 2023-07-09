from streamlitapp import App
import streamlit as st

app = App()

mainpage, standings, predictions, analysis = st.tabs(["Main Page", "Standings", "Predictions", "Analysis"])
with mainpage:
    st.title("Welcome!")
    app.create_mainpage()
with standings:
    st.title("Championship Standings")
    #app.create_standings() # Comment out for api call limits
with predictions:
    st.title("Predictions for the Next Race")
    app.create_predictions()
with analysis:
    st.title("Analysis & KPIs")
    app.create_analysis()