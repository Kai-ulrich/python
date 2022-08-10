# Author : 
# Description : This multi-tool is designed to be used for a variety of purposes

import socket
from geopy.geocoders import Nominatim
import phonenumbers
import platform
from phonenumbers import geocoder, carrier, timezone

# calling the Nominatim tool
geolocator = Nominatim(user_agent="geolocate")

# platform creation
systeminfo = platform.uname()

# user input to decide function
coder = input(" \n Search (1), \n Reverse Search(2), \n Current Device(3), \n Phone # GeoLocate(4), \n System Information(5), \n IP Address(6) \n User> ")

if coder == "1":
    # Location search plus latitude and longitude
    userinput = input("Enter Location: ") 
    # location search
    location = geolocator.geocode(userinput)
    # printing address
    print(location.address)
    # printing latitude and longitude
    print((location.latitude, location.longitude))

elif coder == "2":
    # Print location from latatude and longitude
    latlong = input("Enter Latitude and Longitude: ")
    # location reverse search
    location = geolocator.reverse(latlong)
    # printing address
    print(location.address)

elif coder == "3":
    # print system latatude and longitude
    import geocoder
    g = geocoder.ip('me')
    print(g.latlng)

elif coder == "4":
    # phone number tracing
    userinput = input("Enter Phone Number: ")
    # Notes: + and country codde (1) are mandatory for this to work
    phone_number = phonenumbers.parse("+" + "1" + userinput)
    # Validating a phone number
    valid = phonenumbers.is_valid_number(phone_number)
    # Checking possibility of a number
    possible = phonenumbers.is_possible_number(phone_number)
    
    if valid == True:
        Carrier = carrier.name_for_number(phone_number, "en")
        Region = geocoder.description_for_number(phone_number, "en")
        timeZone = timezone.time_zones_for_number(phone_number)

        print(Carrier)
        print(Region)
        print(timeZone)
    else:
        print(valid)
        print(possible)

elif coder == "5":
    # print system information
    print(f"System: {systeminfo.system}")
    print(f"Node Name: {systeminfo.node}")
    print(f"Version: {systeminfo.version}")
    print(f"Machine: {systeminfo.machine}")
    print(f"Processor: {systeminfo.processor}")

elif coder == "6":
    # print system IP address
    host = socket.gethostbyname(socket.gethostname())
    print(host)

else:
    print("Invalid input")