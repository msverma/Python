import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="🌤️ Weather Dashboard", layout="wide")

st.title("🌍 Real-Time Weather Dashboard")

# User input
city = st.text_input("Enter City Name", "Varanasi")
api_key = "c2b36a89ffc2b7bca75ddf56c32bd4c6"   # OpenWeatherMap से लो

if city:
    # Current Weather
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract fields
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        # Show metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature", f"{temp} °C")
        col2.metric("💧 Humidity", f"{humidity} %")
        col3.metric("☁️ Condition", condition.title())

        # Show icon
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        st.image(icon_url, caption=f"{city_name}, {country}")

        # Show map
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

        # 5-Day Forecast
        st.subheader("📊 5-Day Forecast Trend")
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        forecast_params = {"q": city, "appid": api_key, "units": "metric"}
        forecast_res = requests.get(forecast_url, params=forecast_params)

        if forecast_res.status_code == 200:
            forecast_data = forecast_res.json()
            forecast_list = forecast_data["list"]

            df = pd.DataFrame([{
                "datetime": item["dt_txt"],
                "temp": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "condition": item["weather"][0]["description"]
            } for item in forecast_list])

            df["datetime"] = pd.to_datetime(df["datetime"])

            # Plot chart
            fig, ax = plt.subplots(figsize=(10,5))
            ax.plot(df["datetime"], df["temp"], marker="o", color="blue", label="Temperature (°C)")
            ax.set_title(f"🌤️ 5-Day Temperature Forecast for {city_name}")
            ax.set_xlabel("Date & Time")
            ax.set_ylabel("Temperature (°C)")
            plt.xticks(rotation=45)
            plt.grid(True)
            st.pyplot(fig)

            # Show forecast table
            st.dataframe(df.head(10))
        else:
            st.error("Forecast API error!")
    else:
        st.error("City not found or API error!")
