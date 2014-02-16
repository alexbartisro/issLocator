#Hello!
#This is my first python program
#Feel free to use it however you like but I would appreciate hitting me up at alex.bartis@gmail.com 
#when you use it in one of your cool projects
#GPL V3 licence if it matter
#have fun tracking the ISS


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
		print address;
	except:
		pass;
		print "Current location is unknown";
	printCoordinates();	
	threading.Timer(35, work).start();

def printCoordinates():
        print "The International Space Station's current coordinates are ";
        print "Latitude =",latitude," ","Longitude =",longitude;

work ();
