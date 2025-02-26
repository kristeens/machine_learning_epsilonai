import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.title("Welcome to Our Charity")

df = pd.read_csv(r"new_census.csv")
# Title
st.header("Interactive Visualizations",divider="green")

# Sidebar for user input
with st.sidebar:
    st.subheader("🔧 Choose Your Plot")
    cat_cols = list(df.select_dtypes(include='O').columns)
    num_cols = list(df.select_dtypes(include='number').columns)

    num_choice = st.radio("🔢 Select a Numerical Column", options=num_cols)
    cat_choice = st.selectbox("🔤 Select a Categorical Column", options=cat_cols)

    graph_choice = st.selectbox("📈 Choose a Graph Type", options=['Boxplot', 'Violinplot', 'Stripplot', 'Histogram', 'Pie Chart'])
    

# Graph Selection
choice_to_graph = {
    'Boxplot': px.box, 
    'Violinplot': px.violin, 
    'Stripplot': px.strip, 
    'Histogram': px.histogram, 
    'Pie Chart': px.pie
}

# Graph Button
st.markdown("<br>", unsafe_allow_html=True)  
is_submit = st.button("🎨 Generate Graph")

# Graph output
if is_submit:

    if graph_choice == "Pie Chart":
        fig = choice_to_graph[graph_choice](df, names=cat_choice)
    else:
        fig = choice_to_graph[graph_choice](df, x=cat_choice, y=num_choice)

    st.plotly_chart(fig, use_container_width=True)