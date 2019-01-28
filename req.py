import json,requests
from requests_oauthlib import OAuth1Session

tokenurl = 'https://stage.retsrabbit.com/api/oauth/access_token'
serverurl = 'https://stage.retsrabbit.com/api/v1/server'
apiurl = 'https://stage.retsrabbit.com/api/v1'

class Req():
#    def __init__(self):
#        clientID = open('clientid.txt',"r").read().strip()
#        clientsecret=open('secret.txt',"r").read().strip()
#        print(clientID,clientsecret)
#        getAccessToken()
#        getServerHash()

    clientID = ' '
    clientsecret = ' '
    accesstoken = ' '
    serverhash = ' '

    def getAccessToken(self):
        return self.accesstoken
    def getServerHash(self):
        return self.serverhash
    def getClientID(self):
        return self.clientID
    def getClientSecret(self):
        return self.clientsecret

    def setAccessToken(self):
        data={'grant_type':'client_credentials','client_id':self.clientID,'client_secret':self.clientsecret}
        #print(data)
        r = requests.post(tokenurl,json=data)
        #print(r.url)
        #print(r.text)
        #print(r.status_code,r.reason)
        self.accesstoken = json.loads(r.text)['access_token']
        #print(self.accesstoken)

    def setServerHash(self):
        data={'access_token':self.accesstoken}
        g = requests.get(serverurl,data)
        #print(g.url)
        #print(g.text)
        self.serverhash = json.loads(g.text)[0]['server_hash']
        #print(self.serverhash)

    def initialSearch(self,city,minprice,maxprice):
        city='Columbus'
        searchurl = str(apiurl)+"/"+self.serverhash+"/listing/search"
        data={'ListPrice':str(minprice)+"-"+str(maxprice),'City':city,'access_token':self.accesstoken}
        g = requests.get(searchurl,data)
        #print(g.url)
        #print(json.loads(g.text))        
        #print(g.status_code,g.reason)
        return g

    #def initialSearch(self,city,maxprice):
        #initialSearch(city,0,maxprice)

    def __init__(self):
        self.clientID = open('keys/clientid.txt',"r").read().strip()
        self.clientsecret=open('keys/secret.txt',"r").read().strip()
        #print(self.clientID,self.clientsecret)

        Req.setAccessToken(self)
        Req.setServerHash(self)
