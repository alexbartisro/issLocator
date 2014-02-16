import urllib, json, threading
from pygeocoder import Geocoder

url= "https://api.wheretheiss.at/v1/satellites/25544";
latitude = 0;
longitude = 0;
address = "";

def work():
	global latitude; 
	global longitude; 
        global address;
	print " ";
	response = urllib.urlopen(url);
        data = json.loads(response.read());
        latitude = data['latitude'];
        longitude = data['longitude'];        
	try:
		address =  Geocoder.reverse_geocode(latitude, longitude);
	except:
		pass;
		print "Current location is unknown";
	printCoordinates();	
	print address;
	threading.Timer(35, work).start();

def printCoordinates():
        print "The International Space Station's current coordinates are ";
        print "Latitude =",latitude," ","Longitude =",longitude;

work ();
