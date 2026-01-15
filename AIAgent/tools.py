from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=62918e37cc14ebd45eaab80ea463cc21&query={city}'

  response = requests.get(url)

  return response.json()

tools = [search_tool, get_weather_data]
