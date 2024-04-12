import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from urllib.parse import urlparse


# Function to extract website domain from URL
def extract_website(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Load data from CSV
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')
    data['website'] = data['url'].apply(extract_website)
    return data

# Main function to create the dashboard
def main():
    st.title("News Article Website Analysis")

    # Load data
    data_file_path = r'C:\Users\jabez\OneDrive\Desktop\News Correlation\rating.csv'
    data = load_data(data_file_path)

    # Show data
    st.subheader("Data Preview")
    st.write(data.head())

    # Analyze and display top and bottom websites
    website_counts = data['website'].value_counts()
    sorted_website_data = website_counts.sort_values(ascending=False)
    top_websites = sorted_website_data.head(10)
    bottom_websites = sorted_website_data.tail(10)

    # Plot top and bottom websites side by side
    st.subheader("Top and Bottom 10 Websites with Most and Fewest News Articles")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        top_websites.plot(kind='bar', ax=ax1)
        ax1.set_xlabel('Website')
        ax1.set_ylabel('Number of News Articles')
        ax1.tick_params(axis='x', rotation=45)
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        bottom_websites.plot(kind='bar', ax=ax2)
        ax2.set_xlabel('Website')
        ax2.set_ylabel('Number of News Articles')
        ax2.tick_params(axis='x', rotation=45)
        st.pyplot(fig2)

if __name__ == "__main__":
    main()
data_domain = pd.read_csv(r'C:\Users\jabez\OneDrive\Desktop\News Correlation\domains_location.csv', encoding='utf-8')

# Group data by 'Country' column and count unique values in 'SourceCommonName'
country_counts = data_domain.groupby('Country')['SourceCommonName'].nunique()

# Sort country counts in descending order
sorted_country_counts = country_counts.sort_values(ascending=False)

# Get top and bottom 10 countries
top_countries = sorted_country_counts.head(10)
bottom_countries = sorted_country_counts.tail(10)

# Streamlit App
st.title("Top and Bottom 10 Countries by Number of Unique Sources")
st.subheader("Top 10 Countries")
st.bar_chart(top_countries)

st.subheader("Bottom 10 Countries")
st.bar_chart(bottom_countries)