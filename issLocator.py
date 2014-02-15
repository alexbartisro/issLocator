
import urllib, json, threading

from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

url= "https://api.wheretheiss.at/v1/satellites/25544"

def work():
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        name = data['name']
        latitude = data['latitude']
        longitude = data['longitude']
        threading.Timer(1, work).start();
       	address = geolocator.reverse ("latitude, longitude")
	print " ";
        print "The International Space Station's current coordinates are ";
        print "Latitude =",latitude," ","Longitude =",longitude;
	if address == None:
		print "Current coordinates do not match any known address"
		#uncomment this if you want to print the address even if it is not found
		#print address
	else:
		print "Current address is "
		print " "
		print address
work();
