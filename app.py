import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the transformed data from your local CSV file
df = pd.read_csv('transformed_books_data.csv')

# Descriptive Analytics
st.title('Book Information Analysis')

# Summary Statistics
st.header('Summary Statistics')
st.write(df.describe())

# Correlation Matrix
st.header('Correlation Matrix')
corr_matrix = df.corr()
st.write(corr_matrix)

# Visualizations
st.title('Visualizations')

# Dropdowns for user selection
visualization_type = st.selectbox('Select Visualization Type', ['Histogram', 'Box Plot', 'Bar Chart'])
x_variable = st.selectbox('Select X-Axis Variable', df.columns)
y_variable = st.selectbox('Select Y-Axis Variable', df.columns)

# Plot selected visualization if user has made a selection
if visualization_type and x_variable and y_variable:
    st.header(f'{visualization_type} between {x_variable} and {y_variable}')

    if visualization_type == 'Histogram':
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(data=df, x=x_variable, kde=True, ax=ax)
        st.pyplot(fig)

    elif visualization_type == 'Box Plot':
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.boxplot(data=df, x=x_variable, y=y_variable, ax=ax)
        st.pyplot(fig)

    elif visualization_type == 'Bar Chart':
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(data=df, x=x_variable, y=y_variable, ax=ax)
        st.pyplot(fig)
