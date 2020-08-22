import streamlit as st
import wordcloud
import numpy as np
import plotly.express as px
import plotly.io as pio

# Required configuration to suppress a warning that may occur using file_uploader widget
st.set_option('deprecation.showfileUploaderEncoding', False)

st.write('''# Create a Wordcloud of a Text Document:sunglasses: ''',unsafe_allow_html=True)
st.write("A simple streamlit web app to create an image wordcloud of a text document using the frequency counts of the words.")
def uploader():
    file = st.file_uploader("Upload a Text file")
    if file is not None:
        data = file.getvalue()
        show=st.button("Show Data")
        if show:
            st.write(data)
            st.button("Hide Data")
        
        return data
info=uploader()

def calculate_frequencies(contents):
    # Here is a list of punctuations and uninteresting words whose frequency is generally high in a document \
    # and signifies very less to no importance
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    stopwords = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "other", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    freq = {}
    for word in contents.split():
        if (word.lower() not in stopwords and word.isalpha()==True and word not in punctuations.split()):
            if word.lower in freq:
                freq[word.lower()]+=1
            else:
                freq[word.lower()]=1
    return freq

# calling calculate_frequencies to create a word frequency dictionary of our given data
try:
    freq = calculate_frequencies(info)
except  AttributeError:
        pass
except  NameError:
        st.warning("Upload a file first.")

# Function to create a ndarray that represents our image using WordCloud.generate_from_freuencies method 
def create_wordcloud(freq): 
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()
st.subheader("Wordcloud Image")


def visualize(myimage):
    # Converting the image ndarray into image using imshow from plotly.express package and then displaying it using streamlit.plotly_chart
    wc_img = px.imshow(myimage)
    wc_img.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
    st.plotly_chart(wc_img)
    return wc_img

# calling this to get a ndarray of our wordcloud image and then creating a wordcloud out of that numpy array
try:
    myimage = create_wordcloud(freq)
    img = visualize(myimage)
except NameError:
    pass


