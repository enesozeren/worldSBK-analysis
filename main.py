from streamlitapp import App
import streamlit as st

app = App()

mainpage, standings, predictions = st.tabs(["Main Page", "Standings", "Predictions"])
with mainpage:
    st.title("Welcome!")
    app.create_mainpage()
with standings:
    st.title("Championship Standings")
    # app.create_standings() # Comment out for api call limits
with predictions:
    st.title("Predictions for the Next Race")
    app.create_predictions()