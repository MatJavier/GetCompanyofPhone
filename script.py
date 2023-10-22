import phonenumbers
from phonenumbers import carrier, geocoder, timezone


number = "+1-809-961-0024"


parsed_number = phonenumbers.parse(number)


service_provider = phonenumbers.carrier.name_for_number(parsed_number, "en")
print("Operador del servicio: ", service_provider)


location = geocoder.description_for_number(parsed_number, "en")
print("Ubicación: ", location)


time_zone = timezone.time_zones_for_number(parsed_number)
print("Zona horaria: ", time_zone)
