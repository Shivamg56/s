import streamlit as st
import pandas as pd

# Sample video data (replace with your actual data source)
videos = pd.DataFrame({
    "title": ["Video 1", "Video 2", "Video 3", "Video 4"],
    "description": ["Description 1", "Description 2", "Description 3", "Description 4"],
    "url": ["url_1", "url_2", "url_3", "url_4"],
    "category": ["Category A", "Category B", "Category A", "Category C"]
})

# Function to search videos
def search_videos(query):
  filtered_videos = videos[videos["title"].str.contains(query, case=False) |
                             videos["description"].str.contains(query, case=False)]
  return filtered_videos

# Streamlit app
st.title("My Video Streaming App")

# Search bar
search_query = st.text_input("Search videos")
if search_query:
  results = search_videos(search_query)
  st.write(results)

# Display videos
st.write("All Videos:")
st.write(videos)
