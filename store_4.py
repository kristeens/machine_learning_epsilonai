import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
#import seaborn as sns

st.title("Welcome to Our Charity")
#st.header("ٍStore Visuals",help= "...vs...",divider=True)
st.header("Interactive Visualizations",divider="green")

df = pd.read_csv(r"census.csv")
df1=df.copy()
df1.drop_duplicates(inplace=True)
df1.reset_index(inplace=True,drop=True)

#st.dataframe(df.head())

#df = pd.read_csv(r"E:\epsilon_ai\39\products_details.csv")
tab_1,tab_2,tab_3,tab_4,tab_5 = st.tabs(["Income Range Count","Education_Level vs. Income","Workclass vs. Income","Occupation vs. Income","Race vs. Income"])

with tab_1:
    st.markdown("<center><p><b>As we can see in this graph most of people have income less than or equal 50K </b></p></center>",unsafe_allow_html=True)
    fig = px.histogram(df, x='income')
    st.plotly_chart(fig)
    
with tab_2:
    st.markdown("<p><b>As we can see in this graph the highest ability for charity is for a person of HS-grade and Bachelors degrees as the number of persons with income greater than 50K is 2712 and 2046</b></p>",unsafe_allow_html=True)
    fig1 = px.histogram(df1, y='education_level', color='income')
    st.plotly_chart(fig1)
    
    #dff = df.groupby("Category")[["Total Rates"]].sum().reset_index().sort_values(by="Total Rates",ascending= False)
    #fig = px.pie(names = dff["Category"],values= dff["Total Rates"],title = "Distribution of Total Rates across Category")
    #st.plotly_chart(fig)

with tab_3:
    st.markdown("<p><b>As we can see in this graph the highest ability for charity is for a person that have private work as the number of persons with income greater than 50K is 6156</b></p>",unsafe_allow_html=True)
    fig2 = px.histogram(df1, y='workclass', color='income')
    st.plotly_chart(fig2)
    #df_num = df.select_dtypes(include=np.number)
    #fig1 =px.imshow(df_num.corr(),text_auto = True)
    #st.plotly_chart(fig1)
with tab_4:
    st.markdown("<p><b>As we can see in this graph the highest ability for charity is for a Exec-managerial and Prof-specialty as the number of persons with income greater than 50K is 2489 and 2477 </b></p>",unsafe_allow_html=True)
    fig3 = px.histogram(df1, y='occupation', color='income')
    st.plotly_chart(fig3)
with tab_5:
    st.markdown("<p><b>As we can see in this graph the highest ability for charity is for a White Race as the number of persons with income greater than 50K is 8980 </b></p>",unsafe_allow_html=True)
    fig4 = px.histogram(df1, y='race', color='income')
    st.plotly_chart(fig4)
