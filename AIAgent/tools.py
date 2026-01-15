import os

from dotenv import load_dotenv
import requests
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    if not api_key:
        raise ValueError("WEATHERSTACK_API_KEY is not set")

    url = f"https://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)

    return response.json()

tools = [search_tool, get_weather_data]
