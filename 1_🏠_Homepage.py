import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Twitter Sentiment Analysis App",
    page_icon="🐦",
)

def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_coding  =  load_lottiefile("twitter4.json")
st_lottie(lottie_coding,
                height = 320,
                  width = 320)


st.subheader('Tweeter Sentiment Analysis Classifier On Climate Change ')


st.markdown("""This web app classifies wether or not a person believes climate change is caused by man-kind.
            It classifies tweets or texts regarding climate change into 4 major classes:

- **2 (News)** : the tweet links to factual news about climate change
- **1 (Pro)** : the tweet supports the belief of man-made climate change
- **0 (Neutral)** : the tweet neither supports nor refutes the belief of man-made climate change
- **-1 (Anti)**: the tweet does not believe in man-made climate change Variable definitions




""")














