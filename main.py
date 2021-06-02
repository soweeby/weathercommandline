from geolocator import get_point
from weather import get_forecast_json


def main():
    zipcode = input('Input a zip code')
    coords = get_point(zipcode)  # gets long/lat coords of zipcode for NWS API
    forecast = get_forecast_json(coords)  #
    forecast = forecast[0]
    name = forecast['name']
    detailed_forecast = forecast['detailedForecast']
    print(f"{name}: {detailed_forecast}")


if __name__ == '__main__':
    main()