
import os
import requests
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🌤️ AI Weather Assistant")
st.write("Get weather updates and AI-powered recommendations!")

city = st.text_input("Enter City", "Hyderabad")

if st.button("Get Weather"):
    # Get city coordinates
    location = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}
    ).json()

    if not location.get("results"):
        st.error("City not found!")
        st.stop()

    place = location["results"][0]

    # Get weather data
    data = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": place["latitude"],
            "longitude": place["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation,weather_code",
            "daily": "precipitation_probability_max",
            "timezone": "auto"
        }
    ).json()

    weather = data["current"]
    rain_chance = data["daily"]["precipitation_probability_max"][0]

    st.subheader("🌡️ Current Weather")
    st.write(f"Temperature: {weather['temperature_2m']} °C")
    st.write(f"Humidity: {weather['relative_humidity_2m']}%")
    st.write(f"Wind Speed: {weather['wind_speed_10m']} km/h")
    st.write(f"Precipitation: {weather['precipitation']} mm")
    st.write(f"Today's Maximum Rain Chance: {rain_chance}%")

    # Gemini AI recommendations
    prompt = f"""
    City: {place['name']}
    Current weather data: {weather}
    Today's maximum rain probability: {rain_chance}%

    Based on this weather, recommend:
    1. Clothes to wear
    2. Whether to carry an umbrella
    3. Outdoor activities
    4. Health and safety tips

    Give simple recommendations with emojis.
    Use only the supplied weather data.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.subheader("🤖 AI Recommendations")
    st.write(response.text)

st.caption("Weather data by Open-Meteo")
