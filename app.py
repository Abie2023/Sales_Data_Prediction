import streamlit as st
import home
import data_visulization
import model


#Pages in the app
PAGES = {
    "Home": home,
    "Data Visualization": data_visulization,
    "Data Prediction": model
}

#background styling
page_bg = '''
<style>
body {
background-color : #f4f4f4;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

#navbaar styling
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#292929,#E65142;9);
    color: black;
    align-text: center;
}
hr.rounded {
        border-top: 6px solid #E65142;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True,
)

st.sidebar.title("Explore")

#radio selection for the pages
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#navbar content-2
html4 = '''
<br>
<br>
<p><b>Data Visualization -</b> Analyze the sales data accross various quarters of financial year 2014 for <i>Rossmann Stores</i> using 
multiple charts-box, line, bar, time series etc.</p>
<br>
<p><b>Data Prediction -</b> Predict the future sales set to different features or columns. Predictions can be made using default entries
or select one or multiple fields to be manually edited for predictions.</p>
'''  
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

