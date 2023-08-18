import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import webbrowser

# Get user input for the phone number
number = input("Enter a phone number (with country code): ")

# Parse the phone number
pepnumber = phonenumbers.parse(number)
service_pro = phonenumbers.parse(number)

# Get location information
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

# Get carrier information
service_provider = carrier.name_for_number(service_pro, "en")
print("Service Provider:", service_provider)

# Set up OpenCageGeocode API key
opencage_key = '9fa6367701aa4a40a3518a8aebda3fca'
geocoder = OpenCageGeocode(opencage_key)

# Query location using the parsed location information
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude:", lat)
print("Longitude:", lng)

# Generate a link to open the Google Map
google_map_link = f"https://www.google.com/maps/place/{lat},{lng}"

print("Google Map Link:", google_map_link)

# Automatically open the Google Map link in a web browser
webbrowser.open(google_map_link)
