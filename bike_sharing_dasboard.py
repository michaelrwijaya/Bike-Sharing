import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv('https://raw.githubusercontent.com/michaelrwijaya/AnalisisDataDenganPython/main/streamlit_data.csv')

# Sidebar for filtering options
st.sidebar.title('Filter Options')

# Default filter values covering the entire range
default_season_filter = 'All Seasons'
default_weather_filter = 'All Weather Situations'
default_year_filter = 'All Years'

# Dropdowns with default values
season_filter = st.sidebar.selectbox('Select Season:', ['All Seasons'] + day_df['season'].unique().tolist(), index=0)
weather_filter = st.sidebar.selectbox('Select Weather Situation:', ['All Weather Situations'] + day_df['weathersit'].unique().tolist(), index=0)
year_filter = st.sidebar.selectbox('Select Year:', ['All Years'] + day_df['yr'].unique().astype(str).tolist(), index=0)

# Apply filters if not set to default
if season_filter != 'All Seasons':
    day_df = day_df[day_df['season'] == season_filter]

if weather_filter != 'All Weather Situations':
    day_df = day_df[day_df['weathersit'] == weather_filter]

if year_filter != 'All Years':
    day_df = day_df[day_df['yr'] == int(year_filter)]

# Calculate total counts
total_cnt = day_df['cnt'].sum()
total_casual = day_df['casual'].sum()
total_registered = day_df['registered'].sum()

# Visualizations
st.header('Bike Rentals Dashboard')

# Card Views for total counts
st.subheader('Total Counts')
col1, col2, col3 = st.columns(3)
col1.metric("Total Cnt", total_cnt)
col2.metric("Total Casual", total_casual)
col3.metric("Total Registered", total_registered)

# Bar Plot: Rentals Count by Season and Year
st.subheader('Rentals Count by Season and Year')
bar_fig, ax = plt.subplots(figsize=(10, 6))
bar = sns.barplot(x='season', y='cnt', hue='yr', data=day_df, palette='viridis', ax=ax)
ax.set_xlabel('Season')
ax.set_ylabel('Count')
ax.set_title('Bike Rentals Count by Season and Year')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(title='Year', loc='upper right')
st.pyplot(bar_fig)

# Scatter Plot: Rentals Count vs. Temperature by Season
st.subheader('Rentals Count vs. Temperature by Season')
scatter_fig, ax = plt.subplots(figsize=(10, 6))
scatter = sns.scatterplot(data=day_df, x='temp', y='cnt', hue='season', palette='viridis', ax=ax)
ax.set_xlabel('Temperature')
ax.set_ylabel('Count')
ax.set_title('Bike Rentals Count vs. Temperature by Season')
ax.legend(title='Season', loc='upper left')
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(scatter_fig)

# Bar Plot: Rentals Count Based on Weather Situation
st.subheader('Rentals Count Based on Weather Situation')
weather_fig, ax = plt.subplots(figsize=(10, 6))
weather_bar = sns.barplot(x='weathersit', y='cnt', hue='weathersit', data=day_df, palette='mako', ax=ax)
ax.set_xlabel('Weather Situation')
ax.set_ylabel('Count')
ax.set_title('Bike Rentals Count Based on Weather Situation')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(weather_fig)

# Line Plot: Rentals Count Over Months
st.subheader('Rentals Count Over Months')
line_fig, ax = plt.subplots(figsize=(10, 6))
line = sns.lineplot(data=day_df, x='mnth', y='cnt', ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Count')
ax.set_title('Bike Rentals Count Over Months')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(line_fig)

# Bar Plot: Rentals Count Based on Working Day
st.subheader('Rentals Count Based on Working Day')
working_day_fig, ax = plt.subplots(figsize=(10, 6))
working_day_bar = sns.barplot(x='workingday', y='cnt', hue='workingday', data=day_df, palette='mako', ax=ax)
ax.set_xlabel('Working Day')
ax.set_ylabel('Count')
ax.set_title('Bike Rentals Count Based on Working Day')
for p in working_day_bar.patches:
    working_day_bar.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                             ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8,
                             color='black')
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(working_day_fig)
