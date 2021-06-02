import json
import requests

headers = { 'User-Agent': 'jj'}
URL_BASE = "https://api.weather.gov/points/"


def get_forecast_json(coords):
    """

    :param coords:
    :return:
    """
    latitude = coords[0]
    longitude = coords[1]
    request_url = URL_BASE + f"{latitude},{longitude}"
    initial_response = requests.get(request_url, headers=headers)
    json_response = json.loads(initial_response.content)
    location_properties = json_response["properties"]
    forecast_url = location_properties["forecast"]
    forecast_response = requests.get(forecast_url, headers=headers)
    json_response = json.loads(forecast_response.content)
    forecast_properties = json_response["properties"]
    periods = forecast_properties["periods"]
    return periods
