# 🌤️ AI-Powered Weather App

A simple weather application built using Python, Streamlit, Open-Meteo API, and Google Gemini AI.

I built this project to learn how to integrate APIs with Python and use Generative AI in a real-world application.

The app allows users to search for a city, check its current weather, and get AI-generated recommendations based on the weather conditions.

## 🚀 Features

- Get current weather information for any supported city.
- View temperature, humidity, wind speed, and precipitation.
- Check the day's maximum rain probability.
- Get AI-powered recommendations using Google Gemini.
- Receive suggestions about clothing, outdoor activities, and weather precautions.
- Simple and interactive interface built with Streamlit.

## 🛠️ Technologies Used

- **Python** – Application logic
- **Streamlit** – Web interface
- **Open-Meteo API** – Weather information
- **Google Gemini API** – AI-powered recommendations
- **Requests** – Fetching API data

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/harshavardhan5435r-jpg/AI-Powered-Wheather-App-.git
```

**2. Install the required libraries**

```bash
pip install -r requirements.txt
```

**3. Create a `.env` file and add your Gemini API key**

```env
GEMINI_API_KEY=your_api_key_here
```

**4. Run the application**

```bash
python -m streamlit run app.py
```

## 💡 How It Works

1. The user enters a city name.
2. Open-Meteo provides the city's coordinates and weather information.
3. The app displays the current weather details.
4. Weather data is sent to Google Gemini AI.
5. Gemini generates recommendations based on the weather conditions.

## 📚 What I Learned

While working on this project, I learned:

- How to fetch and use data from REST APIs.
- How to work with JSON responses in Python.
- How to integrate the Gemini API into an application.
- How to create an interactive web interface using Streamlit.
- How to connect real-time weather information with AI-generated recommendations.

## 🔮 Future Improvements

- Add a 7-day weather forecast.
- Improve the UI with weather icons and charts.
- Add support for multiple languages.
- Provide more personalized weather recommendations.

## 📌 Note

Weather data is provided by Open-Meteo. AI-generated recommendations are for general informational purposes.

---

Built as a personal learning project to explore Python, API integration, and Generative AI.
