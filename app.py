import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable use_inf_as_null option
pd.set_option('mode.use_inf_as_null', False)

# Load the CSV file into a Pandas DataFrame
csv_file_path = 'transformed_books_data.csv'
df = pd.read_csv(csv_file_path)

# Set page title
st.set_page_config(page_title='Bookstore Dashboard')

# Custom CSS for styling
st.markdown("""
<style>
    .title-text, .markdown-text-container {
        color: #006400 !important;
    }
    .widget-label {
        color: #483D8B !important;
    }
</style>
""", unsafe_allow_html=True)

st.title('Bookstore Dashboard')

# Filter the DataFrame based on user selection
df_selection = df

# Calculate total number of books, average price, and the sum of the costs of all books
total_books = len(df_selection)
average_price = df_selection['Price'].mean()
total_cost = df_selection['Price'].sum()

# Additional Metrics
unique_titles = len(df['Title'].unique())
average_rating = df['Rating'].mean()

# Metrics Section
st.subheader("Metrics:")
metrics_col1, metrics_col2 = st.columns(2)

with metrics_col1:
    st.metric("Unique Titles", unique_titles)
    st.metric("Average Rating", round(average_rating, 2))

with metrics_col2:
    st.metric("Books available", total_books)
    st.metric("Avg. price of books", f"${round(average_price, 2)}")
    st.metric("Cost of inventory", f"${round(total_cost, 2)}")

# Line to segregate metrics and tables
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Table Section
st.subheader("Top 10 Cheapest Books in the Rating Selected")
top_cheapest_books = df_selection.sort_values('Price').head(10)[['Title', 'Rating', 'Price']]
st.table(top_cheapest_books)

# Line to segregate tables and graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Top 10 Costliest Books
st.subheader("Top 10 Costliest Books in the Rating Selected")
top_costliest_books = df_selection.sort_values('Price', ascending=False).head(10)[['Title', 'Rating', 'Price']]
st.table(top_costliest_books)

# Line to segregate tables and graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Graphs Section
st.subheader("Graphs Section")

# Count of books per rating
fig1, ax1 = plt.subplots()
ax1.pie(df_selection['Rating'].value_counts(), labels=df_selection['Rating'].unique(), autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# Line to segregate graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Price distribution
fig2, ax2 = plt.subplots()
sns.histplot(data=df_selection, x='Price', kde=True, ax=ax2)
st.pyplot(fig2)

# Line to segregate graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Top 10 Best Rated Books
best_rated_books = df_selection.sort_values('Rating', ascending=False).head(10)
fig3, ax3 = plt.subplots()
sns.barplot(data=best_rated_books, x='Title', y='Rating', ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')
st.pyplot(fig3)
