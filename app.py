import streamlit as st
import os

#Work with Core NLP Libraries
from textblob import TextBlob
import spacy
import gensim
import nltk
nltk.download('punkt')

#Sumy Summary Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#Function for Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


#Function to Analyse Tokens and Lemma
def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    #tokens = [token.text for token in docx]
    allData = [('"Token":{}, \n"Lemma":{}'.format(token.text, token.lemma_)) for token in docx ]
    return allData

#The Main Function
def main():
    #Title
    st.title("A policy briefing tool to assist Net Zero policy analysis")
    st.subheader("An internal product to deliver to DITT Economics")
    st.markdown("""
    ###Description
    +This is an app in the testing phased. Developed by Eden Hoang - a DITT graduate for DITT EAA.
    """)

if __name__ == '__main__':
    main()
