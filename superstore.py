import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_icon=":bar_chart:", layout='wide')

st.title(":bar_chart: Superstore Data Dashboard")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)


fl = st.file_uploader(":file_folder: Upload a file", type=['csv', 'xlsx', 'xls', 'txt'])
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding= "ISO-8859-1")
else:
    os.chdir("/Users/belayeth/Documents/Python programming/Python_Streamlit")
    df = pd.read_csv('Superstore.csv', encoding= "ISO-8859-1")
    
    
    #developing the dashboard
    
    Col1, Col2 = st.columns((2))
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    
    #Getting the min and max date
    startDate = pd.to_datetime(df["Order Date"].min())
    endDate = pd.to_datetime(df["Order Date"].max())
    
    with Col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))
    
    with Col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))  
        
    #Filtering the data based on date input
    df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
    
    #Create region filter
    st.sidebar.header("Choose your filter:")   
    region = st.sidebar.multiselect("Select your region:",
                                    options=df["Region"].unique(),
                                    default=df["Region"].unique())

    if not region:
        df2 = df.copy()
    else:
        df2 = df [df["Region"].isin(region)]
        
#Create state filter
    state = st.sidebar.multiselect("Select your state:",
                                    options=df2["State"].unique(),
                                    default=df2["State"].unique())   

    if not state:
        df3 = df2.copy()
    else:
        df3 = df [df["State"].isin(state)]   
        
        
#Create filter for city
    city = st.sidebar.multiselect("Select your city:",
                                    options=df3["City"].unique(),
                                    default=df3["City"].unique())   

    if not city:
        df4 = df3.copy()
    else:
        df4 = df3 [df3["City"].isin(city)]