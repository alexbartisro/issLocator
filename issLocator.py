
import urllib, json, threading
from geopy import geocoders

geolocator =  geocoders.GoogleV3()
url= "https://api.wheretheiss.at/v1/satellites/25544";
latitude = 0;
longitude = 0;
address = "";
lastKnownAddress = "";
point = ""; 

def work():
	global latitude; 
	global longitude; 
	global address; 
	global lastKnownAddress; 
	global point;
        response = urllib.urlopen(url);
        data = json.loads(response.read());
        name = data['name'];
        latitude = data['latitude'];
        longitude = data['longitude'];
       	strLong = '%.7f' % longitude;
	strLat = '%.7f' % latitude;
	point = strLat + ", " + strLong; 
	threading.Timer(1, work).start();
       	address = geolocator.reverse ("latitude", "longitude");
	if address != None:
		lastKnownAddress = address;
	printCoordinates();	

def printCoordinates():
	print "Point is ", point;
	print " ";
        print "The International Space Station's current coordinates are ";
        print "Latitude =",latitude," ","Longitude =",longitude;
	if ( lastKnownAddress != None and lastKnownAddress !="" ):
	#	print "Current address is ";
	#	print address;
		print "Last known Address is ";
		print lastKnownAddress;
		

work();
