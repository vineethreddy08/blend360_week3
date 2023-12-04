import streamlit as st
import pandas as pd
import plotly.express as px

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
st.subheader("Most Affordable Books in the store")
top_cheapest_books = df_selection.sort_values('Price').head(10)[['Title', 'Rating', 'Price']]
st.table(top_cheapest_books)

# Line to segregate tables and graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Top 10 Costliest Books
st.subheader("10 Most expensive Books in the store")
top_costliest_books = df_selection.sort_values('Price', ascending=False).head(10)[['Title', 'Rating', 'Price']]
st.table(top_costliest_books)

# Line to segregate tables and graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Graphs Section
st.subheader("Graphs Section")

# Count of books per rating
fig1 = px.pie(
    df_selection,
    names='Rating',
    title='Distribution of Rating',
    labels={'Rating': 'Rating'},
)

# Line to segregate graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Price distribution
fig2 = px.histogram(df_selection, x='Price', nbins=20, labels={'Price': 'Price'}, title='Distribution of Prices')

# Line to segregate graphs
st.markdown('<hr style="border:1px solid #483D8B">', unsafe_allow_html=True)

# Top 10 Best Rated Books
best_rated_books = df_selection.sort_values('Rating', ascending=False).head(10)
fig3 = px.bar(
    best_rated_books,
    x='Title',
    y='Rating',
    title="<b>Top 10 Best Rated Books</b>"
)
fig3.update_layout(xaxis_tickangle=-45)

# Display Graphs
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
