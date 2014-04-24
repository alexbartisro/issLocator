"""
ISS Locator by Trusk89:alex.bartis@gmail.com 
Edited / Shortened / Made Worse by SgtBurned:SgtBurned@hotmail.co.uk
"""

import urllib, json, time
from pygeocoder import Geocoder

url= "https://api.wheretheiss.at/v1/satellites/25544"
lat = lon = addr = False

def Read():
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	lat = data['latitude']
	lon = data['longitude']
	try:
		addr =  Geocoder.reverse_geocode(lat, lon)
	except:
		return False, False, False
	return lat, lon, addr

if __name__ == "__main__":
	while 1:
		lat, lon, addr = Read()
		print "The ISS is located at:\nLat: {}\nLon: {}\nAddress: {}".format(lat, lon, addr)
		time.sleep(15)
