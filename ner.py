#IMPORT IMPORTANT LIBRARIES
import streamlit as st
import wikipedia
import spacy
from spacy import displacy
from bs4 import BeautifulSoup
from urllib.request import urlopen

#ENGLISH PIPELINE OPTIMIZED FOR CPU
#COMPONENTS: tok2vec, tagger, parser, senter, ner, attribute_ruler, lemmatizer
nlp = spacy.load("en_core_web_sm")

#HTML STYLING
HTML_WRAPPER = """<div style="overflow-x: auto; border: 0 solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

#TO EXTRACT CONTENT FROM INPUT URL
@st.cache
def text_url(url):
    page=urlopen(url)
    soup=BeautifulSoup(page)
    text_extracted=' '.join(map(lambda p:p.text,soup.find_all('p')))
    return text_extracted
#MAIN FUNCTION
def main():
    st.title("Named Entity Recognition")
    operations=["Name Enitity Recognition: Summary","Name Enitity Recognition: URL"]
    #SIDEBAR FOR SELECTING BETWEEN TWO OPERATIONS
    choice=st.sidebar.selectbox("Select Operation",operations)

    if choice=="Name Enitity Recognition: Summary":
        st.subheader("Entities Recognition With Spacy")
        text_box=st.text_input("Enter Page Name")
        if st.button("Check"):
            doc=nlp(wikipedia.summary(text_box))
            all_sentence=list(doc.sents)
            html=displacy.render(all_sentence,style='ent')
            html=html.replace("\n\n","\n")
            
            st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
    
    if choice=="Name Enitity Recognition: URL":
        st.subheader("Entities Recognition With Spacy")
        url=st.text_input("Enter URL")
        if st.button("Check"):
            result=text_url(url)
            doc=nlp(result)  
            all_sentence=list(doc.sents)
            html=displacy.render(all_sentence,style='ent')
            html=html.replace("\n\n","\n")
            
            st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)     

if __name__=='__main__':
    main()

