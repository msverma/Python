import requests
import streamlit as st

st.title("🌤️ Real-Time Weather Forecast")

city = st.text_input("Enter city name", "Varanasi")
api_key = "c2b36a89ffc2b7bca75ddf56c32bd4c6"  # OpenWeatherMap से लो

if city:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        city= data['name']
        country= data['sys']['country']
        icon= data["weather"][0]["icon"]

        st.success(f"🌡️ Temperature: {temp}°C")
        st.info(f"💧 Humidity: {humidity}%")
        st.write(f"☁️ Condition: {condition}")
        st.info(f"City: {city}")
        st.info(f'Country: {country}')
        st.info(f'Icon: {icon}')
    else:
        st.error("City not found or API error!")
