import streamlit as st
from PIL import Image

st.title('Exploratory Data Analysis')


st.markdown(""" Exploratory Data Analysis is a very important aspect of machine learning. It refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.


It is a good practice to understand the data first and try to gather as many insights from it. EDA is all about making sense of data in hand,before getting them dirty with it.

Druing EDA of of dataset, we carried out both graphical and non graphical analysis of our dataset and discovered the following insights


1. Number of People with positive sentitiments i.e people who believe that climate change is man-made was higher than other classes.

See Barchart below.

""")


image = Image.open('resources/sentiment_c.png')
st.image(image, width=500)


st.markdown("""2. Most popular users and their sentiments 

See Barchart below.""")

image = Image.open('resources/users.png')
st.image(image, width=600)

st.markdown("""3. Top 10 users with "Pro" Sentiments.""")

image = Image.open('resources/top10.png')
st.image(image, width=500)

st.markdown("""4. Top 10 users with "Anti" Sentiments.""")

image = Image.open('resources/anti.png')
st.image(image, width=500)

st.markdown("""5. Word Cloud of the most common words: A word cloud is a collection, or cluster, of words depicted in different sizes. The bigger and bolder the word appears, the more often it’s mentioned within a given text and the more important it is.""")

image = Image.open('resources/word cloud.png')
st.image(image, width=500)


st.markdown("""6. Word Cloud of trending HastTags """)

image = Image.open('resources/word cloud.png')
st.image(image, width=500)













