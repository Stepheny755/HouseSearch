import requests,json
import googlemaps

class Map():

    apikey = ''
    gmaps = ''

    def __init__(self):
        self.apikey = open('keys/apikey.txt',"r").read().strip()
        self.gmaps = googlemaps.Client(key=self.apikey)
        #print(self.apikey)
        #data={'origin':'Disneyland','destination':'Universal+Studios','key':self.apikey}
        #g = requests.get(apiend,data)
        #print(g.url)
        #print(g.text)

    def getGeoCode(self,address):
        geocode_result = self.gmaps.geocode(str(address))
        return(geocode_result[0]['geometry']['location']['lat'],geocode_result[0]['geometry']['location']['lng'])

    def getAddress(self,coordx,coordy):
        reverse_result = self.gmaps.reverse_geocode((coordx,coordy))
        return reverse_result

    def getDistanceTime(self,orig,dest):
        #print(self.gmaps.directions(orig,dest))
        dirs = self.gmaps.directions(orig,dest)[0]['legs'][0]['duration']['value']
        
        #print(self.gmaps.directions(orig,dest)[0])
        return dirs


