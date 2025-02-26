import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator

# OutlierHandler Function

class OutlierHandler(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self 

    def transform(self, X, y=None):
        X = pd.DataFrame(X).copy()  
        for col in X.columns:
            q1 = np.percentile(X[col], 25)
            q3 = np.percentile(X[col], 75)
            iqr = q3 - q1
            ub = q3 + 1.5 * iqr
            lb = q1 - 1.5 * iqr
            X[col] = np.clip(X[col], lb, ub) 
        return X
    def get_feature_names_out(self, input_features=None):
        return input_features if input_features is not None else []
    
# CustomTransformer Function
    
class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, log_columns=None):
        self.log_columns = log_columns if log_columns else []

    def fit(self, X, y=None):
        return self  

    def transform(self, X, y=None):
        X = pd.DataFrame(X).copy()  
        for col in self.log_columns:
            X[col] = np.log1p(X[col]) 
        return X
    def get_feature_names_out(self, input_features=None):
        return input_features if input_features is not None else []
    
# Load the preprocessor
pipeline = joblib.load("preprocessor.pkl")
feature_names = np.load("feature_names.npy", allow_pickle=True)

# Load the trained model
model = joblib.load('best_model.pkl') 

# Page Design

st.set_page_config(page_title="Income Prediction", page_icon="💰", layout="wide")

# Title

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Income Prediction </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #4B7BFF;'>Predict your volunteers category based on your personal details</h4>", unsafe_allow_html=True)

st.divider()

# Inputs Design

col1, col2, col3 = st.columns(3)

with col1:
    sex = st.radio("👤 **Sex**", ['Male', "Female"])  
    age = st.slider("🎂 **Age**", min_value=17, max_value=90)
    education_num = st.select_slider("🎓 **Education Level**", options=[str(i) for i in range(3, 17)])
    marital_status = st.selectbox("💍 **Marital Status**", [' Never-married', ' Married-civ-spouse' ,' Divorced',
 ' Married-spouse-absent', ' Separated' ,' Married-AF-spouse', ' Widowed'])
    workclass = st.selectbox("🏢 **Workclass**", [' State-gov' ,' Self-emp-not-inc', ' Private', ' Federal-gov', ' Local-gov',
 ' Self-emp-inc' ,' Without-pay'])

with col2:
    occupation = st.selectbox("🛠 **Occupation**", [' Adm-clerical' ,' Exec-managerial', ' Handlers-cleaners', ' Prof-specialty'
 ' Other-service', ' Sales', ' Transport-moving' ,' Farming-fishing',' Machine-op-inspct', ' Tech-support' ,' Craft-repair' ,' Protective-serv',
 ' Armed-Forces', ' Priv-house-serv'])
    Work_Life_Balance = st.selectbox("⚖️ **Work-Life Balance**", ['Good Balance', 'High Balance', 'Low Balance', 'Moderate Balance'])
    capital_gain = st.number_input("📈 **Capital Gain**", min_value=1, max_value=99999, step=100)
    capital_loss = st.number_input("📉 **Capital Loss**", min_value=1, max_value=4356, step=10)
    Income_per_Hour = st.number_input("💰 **Income Per Hour**", min_value=1, max_value=11365, step=5)

with col3:
    race = st.selectbox("🌎 **Race**", [' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',' Other']) 
    native_country = st.selectbox("🏳️ **Native Country**", [' United-States', ' Cuba', ' Jamaica', ' India', ' Mexico',' Puerto-Rico', 
        ' Honduras', ' England', ' Canada', ' Germany',' Iran', ' Philippines', ' Poland', ' Columbia', ' Cambodia',' Thailand', 
        ' Ecuador', ' Laos', ' Taiwan', ' Haiti', ' Portugal',' Dominican-Republic', ' El-Salvador', ' France', ' Guatemala',
       ' Italy', ' China', ' South', ' Japan', ' Yugoslavia', ' Peru',' Outlying-US(Guam-USVI-etc)', ' Scotland', ' Trinadad&Tobago',
       ' Greece', ' Nicaragua', ' Vietnam', ' Hong', ' Ireland',' Hungary', ' Holand-Netherlands'])
    relationship = st.selectbox("👨‍👩‍👧‍👦 **Relationship**", [' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried',
       ' Other-relative'])
    Age_Ranges = st.selectbox("📅 **Age Range**", ['Young Middle-Age', 'Adult', 'Young Adulthood', 'Child', 'Seniors'])


input_features = {
    "age": age,
    'workclass': workclass,
    'education-num':education_num,
    "marital-status": marital_status,
    "occupation": occupation,
    'relationship': relationship,
    'race':race,
    "sex": sex,
    "capital-gain": capital_gain,
    "capital-loss": capital_loss,
    'native-country': native_country,
    'Age Ranges': Age_Ranges,
    'Work_Life_Balance': Work_Life_Balance,
    "Income_per_Hour": Income_per_Hour
}  
# Prepare data for predection
 
input_df = pd.DataFrame([input_features])
input_data_transformed = pipeline.transform(input_df)
input_df_transformed = pd.DataFrame(input_data_transformed, columns=feature_names)

categorical_columns = [
    "workclass", "education-num", "marital-status", "occupation", 
    "relationship", "race", "sex", "native-country", "Age Ranges", 
    "Work_Life_Balance"
]

if not input_df_transformed.empty:
    for col in input_df_transformed.select_dtypes(include=['category']).columns:
        input_df_transformed[col] = input_df_transformed[col].cat.codes  

for col in input_df_transformed.select_dtypes(include=['object']).columns:
    try:
        input_df_transformed[col] = input_df_transformed[col].astype(float) 
    except ValueError:
        print(f"Column '{col}' contains non-numeric values and will be removed!")  
        input_df_transformed.drop(columns=[col], inplace=True)  

non_numeric_cols = input_df_transformed.select_dtypes(exclude=['int64', 'float64']).columns

if len(non_numeric_cols) > 0:
    print(f"Warning: The following columns are still non-numeric and will be removed: {non_numeric_cols.tolist()}")
    input_df_transformed.drop(columns=non_numeric_cols, inplace=True)
print("DataFrame after processing:", input_df_transformed.dtypes)

# Prediction

if st.button("Predict Income"):
    prediction = model.predict(input_df_transformed)
    result = "≤50K" if prediction == 0 else ">50K"
    st.success(f"Predicted Income Category: **{result}**")
