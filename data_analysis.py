import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title
st.title("Data Analysis and Visualization")

# Sidebar
st.sidebar.subheader("Visualization Settings")

# File upload
uploaded_file = st.sidebar.file_uploader(
                         label="Upload your CSV or Excel file. (200 MB Max)",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)  
        
# Allows user to upload their dataset
global numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float','int']).columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")
    
    
# Adds a chart select widget on a sidebar
chart_select = st.sidebar.selectbox(
    label="Select the Chart Type",
options=['Scatterplot', 'Lineplot', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplot':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values= st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values= st.sidebar.selectbox('Y axis', options=numeric_columns)
        scatterplot = px.scatter(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(scatterplot)
    except Exception as e:
        print(e)

if chart_select == 'Lineplot':
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_values= st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values= st.sidebar.selectbox('Y axis', options=numeric_columns)
        lineplot = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(lineplot)
    except Exception as e:
        print(e)


if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x_values= st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values= st.sidebar.selectbox('Y axis', options=numeric_columns)
        histogram = px.histogram(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(histogram)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        x_values= st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values= st.sidebar.selectbox('Y axis', options=numeric_columns)
        boxplot = px.box(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(boxplot)
    except Exception as e:
        print(e)

# Calculates statistical results of the data
if uploaded_file is not None:
    if st.checkbox("Overall Statistics"):
        st.write(df.describe())

# Checks the shape of the data
if uploaded_file is not None:
    df_shape = st.radio("What Dimension Do You Want To Check?", ('Rows',
                                                                   'Columns'))
    if df_shape=='Rows':
        st.text("Number of Rows")
        st.write(df.shape[0])
    if df_shape=='Columns':
        st.text("Number of Columns")
        st.write(df.shape[1])
        
#Checks for Null Values
if uploaded_file is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(df.isnull())
            st.pyplot()
        else:
            st.success("No Missing Values")
            
# Finds Duplicate Values
if uploaded_file is not None:
    test=df.duplicated().any()
    if test==True:
        st.warning("This Datset Contains Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            df_duplicates=df.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Duplicates Values not Removed")          
        
