- 👋 Hi, I’m @DiyoTempest
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...import phonenumbers
import opencage
import folium
from myphone import numbers

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber , "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en")) 

from opencage.geocoder import OpenCageGeocode

key = 'a9c5b28b233c4f8bd91a903e67489d'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat.lng], popup=location). add_to(myMap)
myMap.save("Mylocation.html")
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
DiyoTempest/DiyoTempest is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
