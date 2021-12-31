import phonenumbers
import opencage
import folium
from mynumber import NumberPhone
from phonenumbers import geocoder

# Getting a country location
numb = phonenumbers.parse(NumberPhone)
location = geocoder.description_for_number(numb, "en")
print(location)

from phonenumbers import carrier

# Getting a provider name
provider = phonenumbers.parse(NumberPhone)
print(carrier.name_for_number(provider, "en"))

from opencage.geocoder import OpenCageGeocode

api_key = 'your_opencage_api_here'

geocoder = OpenCageGeocode(api_key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat, lng)

maps = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(maps)
maps.save('output.html')
