import phonenumbers
from phonenumbers import geocoder, carrier, timezone

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