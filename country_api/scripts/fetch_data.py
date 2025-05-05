import requests
import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'country_app.settings')
django.setup()

from country_api.models import Country


def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        countries_data = response.json()

        # Clear existing data
        Country.objects.all().delete()

        # Process and save each country
        for country_data in countries_data:
            try:
                country = Country(
                    name_common=country_data.get('name', {}).get('common', 'Unknown'),
                    name_official=country_data.get('name', {}).get('official', 'Unknown'),
                    cca2=country_data.get('cca2', ''),
                    capital=country_data.get('capital', []),
                    population=country_data.get('population', 0),
                    timezones=country_data.get('timezones', []),
                    region=country_data.get('region', ''),
                    subregion=country_data.get('subregion', ''),
                    languages=country_data.get('languages', {}),
                    flag_png=country_data.get('flags', {}).get('png', ''),
                    flag_svg=country_data.get('flags', {}).get('svg', ''),
                    flag_emoji=country_data.get('flag', '')
                )
                country.save()
                print(f"Saved {country.name_common}")
            except Exception as e:
                print(f"Error saving {country_data.get('name', {}).get('common', 'Unknown')}: {e}")

        print(f"Successfully imported {Country.objects.count()} countries")
    else:
        print(f"Failed to fetch data: {response.status_code}")


if __name__ == "__main__":
    fetch_countries()