import streamlit as st
import pandas as pd
df = pd.read_csv(r"census.csv")
st.header("Understand Data",divider="green")

tab_1,tab_2 = st.tabs(["About Census","Columns Definition"])

with tab_1:
    st.markdown("<center><p><b>The US Adult Census dataset is a repository of 45,221 entries extracted from the 1994 US Census database</b></p></center>",unsafe_allow_html=True)
    df = pd.read_csv(r"census.csv")
    st.dataframe(df.head())
    
with tab_2:
    st.markdown("<p><b>The Census Income dataset has 45,221 entries.Each entry contains the following information about an individual:</b><br><p><b>● Age</b>​ :The age of an individual Integer greater than 0.</p><br><p><b>● Workclass</b>​ : A general term to represent the employment status of an individual.</p><br><p><b>● Education​ :</b> The highest level of education achieved by an individual.</p><p><b>● Education ­Num​ :</b> The highest level of education achieved in numerical form.</p><p><b>● Marital ­Status​ :</b> Marital Status of an individual. <b>Married ­civ ­spouse</b> corresponds to acivilian spouse while <b>Married ­AF ­spouse</b> is a spouse in the Armed Forces.</p><br><p><b>●Occupation​ :</b> The general type of occupation of an individual.</p><br><p><b>●Relationship​ :</b> Represents what this individual is relative to others. For example an individual could be a Husband. Each entry only has one relationship attribute and is somewhat redundant with marital status.</p><br><p><b>●Race​ :</b> Descriptions of an individual’s race</p><br><p><b>●Sex​ :</b> The biological sex of the individual</p><br><p><b>●Capital­ Gain​ :</b> Capital Gains for an individual <br><p><b>● Capital ­Loss​ :</b> Capital Loss for an individual.</p><br><p><b>● Hours­Per­Week​ :</b> The hours an individual has reported to work per week.</p><br><p><b>● Native ­Country​ :</b> country of origin for an individual.</p><br><p><b>● Income​ :</b> Whether or not an individual makes more othan $50,000 annually.</p>"
,unsafe_allow_html=True)
