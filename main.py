
import streamlit as st
from function import load_data, data_distribution, relationship, comparison, composition, clustering, data_storytelling
from streamlit_option_menu import option_menu

with st.sidebar:

    selected = st.selectbox("Mall Customer Segmentation", ["Introducing", "Data Visualization", "Clustering"])

    if selected == "Data Visualization":
        pilih = option_menu(
        menu_title="", 
        options=["Distribution", "Relationship", "Comparison", "Composition"],
        default_index=0)

def display_introducing():
    cs = load_data()
    data_storytelling(cs)

def display_data_distribution():
    cs = load_data()
    data_distribution(cs)

def display_relationship():
    cs = load_data()
    relationship(cs)

def display_comparison():
    cs = load_data()
    comparison(cs)

def display_composition():
    cs = load_data()
    composition(cs)

def display_clustering():
    clustering()

if selected == "Introducing":
    display_introducing()
    
elif selected == "Data Visualization":
    if pilih == "Distribution":
        display_data_distribution()
    elif pilih == "Relationship":
        display_relationship()
    elif pilih == "Comparison":
        display_comparison()
    elif pilih == "Composition":
        display_composition()

elif selected == "Clustering":
    display_clustering()