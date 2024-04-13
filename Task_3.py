import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from urllib.parse import urlparse


def extract_website(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc


@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')
    data['website'] = data['url'].apply(extract_website)
    return data


@st.cache
def load_country_data(file_path):
    data_domain = pd.read_csv(file_path, encoding='utf-8')
    return data_domain


def main():
    

    country_data_path = r'C:\Users\jabez\OneDrive\Desktop\News Correlation\domains_location.csv'
    data_domain = load_country_data(country_data_path)

    
    country_counts = data_domain.groupby('Country')['SourceCommonName'].nunique()

    sorted_country_counts = country_counts.sort_values(ascending=False)

    top_countries = sorted_country_counts.head(10)
    bottom_countries = sorted_country_counts.tail(10)

    
    st.title("Top and Bottom 10 Countries by Number of Unique Sources")
    st.subheader("Top 10 Countries")
    st.bar_chart(top_countries)

    st.subheader("Bottom 10 Countries")
    st.bar_chart(bottom_countries)

if __name__ == "__main__":
    main()


def main():
    
    country_data_path = r'C:\Users\jabez\OneDrive\Desktop\News Correlation\domains_location.csv'
    data_domain = load_country_data(country_data_path)
    country_data_path = r'C:\Users\jabez\OneDrive\Desktop\News Correlation\rating.csv'
    data = load_country_data(country_data_path)
   
   
   
    

    country_names = data_domain['Country'].tolist()
    country_data = data[data['category'].isin(country_names)]
    country_talking_counts = country_data['category'].value_counts()
    sorted_country_talking = country_talking_counts.sort_values(ascending=False)
    top_10_countries = sorted_country_talking.head(10)
    bottom_10_countries = sorted_country_talking.tail(10)

    
    st.title("Countries that have many articles written about them")
    st.subheader("Top 10 Countries")
    st.bar_chart(top_10_countries)

    st.subheader("Bottom 10 Countries")
    st.bar_chart(bottom_10_countries)

if __name__ == "__main__":
    main()


data_path = r'C:\Users\jabez\OneDrive\Desktop\News Correlation\rating.csv'
data = pd.read_csv(data_path)
data['website'] = data['url'].apply(extract_website)
african_countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo",
"Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Eswatini", "Gabon", "Gambia", "Ghana", "Guinea", 
"Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
"Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
"South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

europian_countries= ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", 
"Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland",
"Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro",
"Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
"Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom"]

middle_east =["Bahrain", "Cyprus", "Egypt", "Iran", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Qatar", "Saudi Arabia", "Syria",
"Turkey", "United Arab Emirates", "Yemen"]

united_states = ['United States']
china = ['China']
russia = ['Russia']
ukraine = ['Ukraine']

def news_count_per_group(group_name, data):
    group_data = data[data['category'].isin(group_name)]
    group_website_counts = group_data['website'].value_counts()
    sorted_group_website_count = group_website_counts.sort_values(ascending=False)
    top_10_group_websites = sorted_group_website_count.head(10)
    bottom_10_group_websites = sorted_group_website_count.tail(10)

    st.write(f"<p style='font-size:12px'>Top 10 Websites for {group_name}</p>", unsafe_allow_html=True)
    st.bar_chart(top_10_group_websites)
    
    st.write(f"<p style='font-size:12px'>Bottom 10 Websites for {group_name}</p>", unsafe_allow_html=True)
    st.bar_chart(bottom_10_group_websites)

# Streamlit App
def main():
    st.title("News Article Website Analysis")

    group_name = st.selectbox(
        "Select a group of countries",
        ["African Countries", "European Countries", "Middle East", "United States", "China", "Russia", "Ukraine"]
    )

    if group_name == "African Countries":
        news_count_per_group(african_countries, data)
    elif group_name == "European Countries":
        news_count_per_group(europian_countries, data)
    elif group_name == "Middle East":
        news_count_per_group(middle_east, data)
    elif group_name == "United States":
        news_count_per_group(united_states, data)
    elif group_name == "China":
        news_count_per_group(china, data)
    elif group_name == "Russia":
        news_count_per_group(russia, data)
    elif group_name == "Ukraine":
        news_count_per_group(ukraine, data)

if __name__ == "__main__":
    main()
