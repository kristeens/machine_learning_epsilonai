import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 45px !important;
            font-weight: bold;
            color: #ff914d;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #444;
            text-align: center;
        }
        .stButton > button {
            width: 60%;
            background-color: #ff914d;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
            margin: auto;
            display: block;
        }
        .stButton > button:hover {
            background-color: #e87c3d;
        }
        .stImage {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Display title and subtitle
st.markdown('<p class="title">✨ Welcome to Our Orphans Charity ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Providing hope, love, and a better future for orphans ❤️</p>', unsafe_allow_html=True)

# Display animated GIF instead of static image
st.image("charity_animation.gif", use_container_width=True)


