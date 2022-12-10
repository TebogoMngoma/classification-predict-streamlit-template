import streamlit as st
from PIL import Image

st.title('Feature Engineering And Data Cleaning')

st.subheader("What's Feature Engineering?🤔")

st.markdown("""Feature engineering is the process of selecting, manipulating, and transforming raw data into features that can be used in supervised learning.
Feature Engineering is a very important step in machine learning as it helps to boost model performances with these artificials features created.

When feature engineering activities are done correctly, the resulting dataset is optimal and contains all of the important factors that affect the business problem. As a result of these datasets, the most accurate predictive models and the most useful insights are produced.
### Feature Engineering Techniques Used In Our Model Development

Some feature engineering techniques applied during this project include;


- Removal of URLs/Website Link from or dataset using regular expressions

- Converting all texts to lowercase

- Removing punctuations and special characters

- Tokenization (o split paragraphs and sentences into smaller units that can be more easily assigned meaning)

- Lematization (a text normalization technique used in Natural Language Processing (NLP), that switches any kind of a word to its base root mode)

- Vectoriing Tweets so our model can understand our input and give a corresponding output

- Balancing the distribution of classes in the target variable (this is imperative to yield better model performance""")




st.markdown(""" Lets take a look at some visuals before and after feature engineering and data cleaning""")
image = Image.open('resources/numcharacters.png')
st.image(image, width=500)











