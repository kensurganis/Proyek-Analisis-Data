import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_resource
def load_data():
    data = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return data

data = load_data()

st.title("Dashboard Bike-Share")

st.sidebar.title("Bio:")
st.sidebar.markdown("Nama: Kens Urganis Awangsari Puttrisia Soenarto")
st.sidebar.markdown(
    "Email: [M258d4kx1912@bangkit.academy]")
st.sidebar.markdown(
    "Dicoding: [M258d4kx1912]")

st.sidebar.title("Dataset Bike-Share")

if st.sidebar.checkbox("Dataset"):
    st.subheader("Data")
    st.write(data)

if st.sidebar.checkbox("Statistik Dataset"):
    st.subheader("Statistik")
    st.write(data.describe())

col1, col2 = st.columns(2)

with col1:
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["season_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("season_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season_label", y="cnt", title="Season-wise Bike Share Count")
    st.plotly_chart(fig_season_count, use_container_width=True, height=400, width=600)
    
with col2:
    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit", y="cnt", title="Weather Situation-wise Bike Share Count")
   
    st.plotly_chart(fig_weather_count, use_container_width=True,height=400, width=800)
    
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True, height=400, width=600)

fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart)

fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

fig_temp_chart = px.scatter(data, x="temp", y="cnt", title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True, height=400, width=800)

st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")