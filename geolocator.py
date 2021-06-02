import json
import requests

KEY = ""  # bing maps api key
URL_BASE = "http://dev.virtualearth.net/REST/v1/Locations?"


def get_location(zipcode):
    """
    :param zipcode: zipcode (string) to find location properties of
    :return: resources (dictionary which contains city, county, coords, etc.)
    """
    api_url = URL_BASE + f"postalCode={zipcode}&key={KEY}"
    response = requests.get(api_url)
    json_response = json.loads(response.content)  # entire json response
    resource_sets = json_response['resourceSets'][0]
    resources = resource_sets['resources'][0]
    return resources


def get_point(zipcode):
    """
    gets latitude and longitude coordinates for a given zipcode
    :param zipcode:
    :return: coords (list of latitude and longitude coordinates)
    """
    resources = get_location(zipcode)
    point = resources['point']
    coords = point['coordinates']
    return coords



