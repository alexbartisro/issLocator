
import urllib, json, threading
from pygeocoder import Geocoder

url= "https://api.wheretheiss.at/v1/satellites/25544";
latitude = 0;
longitude = 0;
address = "";
lastKnownAddress = "";

def work():
	global latitude; 
	global longitude; 
	global address; 
	global lastKnownAddress; 
        response = urllib.urlopen(url);
        data = json.loads(response.read());
        latitude = data['latitude'];
        longitude = data['longitude']; 
	try:       
		address = Geocoder.reverse_geocode(latitude, longitude);
	except ValueError:
		print "No known address";
	if address != None:
		lastKnownAddress = address;
	printCoordinates();	
	threading.Timer(1, work).start();


def printCoordinates():
	print " ";
	print "Last know address is ", lastKnownAddress;
        print "The International Space Station's current coordinates are ";
        print "Latitude =",latitude," ","Longitude =",longitude;
#	if ( lastKnownAddress != None and lastKnownAddress !="" ):
	#	print "Current address is ";
	#	print address;
#		print "Last known Address is ";
#		print lastKnownAddress;

work();
