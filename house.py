

class House():

    lat=0
    lng=0
    id=0

    edutime=0
    worktime=0
    other1time=0
    other2time=0
    other3time=0

    affinity=0

    ranking = []

    def __init__(self):
        pass

    def __init__(self,id,lat,lng):
        self.id = id
        self.lat = lat
        self.lng = lng
        self.affinity = 0

    def __str__(self):
        temp = self.id+' '+self.lat+' '+self.lng
        if(self.worktime!=0):
            temp+=' '+str(self.worktime)
        if(self.edutime!=0):
            temp+=' '+str(self.edutime)
        if(self.other1time!=0):
            temp+=' '+str(self.other1time)
        if(self.other2time!=0):
            temp+=' '+str(self.other2time)
        if(self.other3time!=0):
            temp+=' '+str(self.other3time)
        return temp

    def setETime(self,time):
        self.edutime=time
    def setWTime(self,time):
        self.worktime=time
    def set1Time(self,time):
        self.other1time=time
    def set2Time(self,time):
        self.other2time=time
    def set3Time(self,time):
        self.other3time=time

    def getETime(self):
        return self.edutime
    def getWTime(self):
        return self.worktime
    def get1Time(self):
        return self.other1time
    def get2Time(self):
        return self.other2time
    def get3Time(self):
        return self.other3time
        
    def setAffinity(self,a):
        self.affinity = a

    def getAffinity(self):
        return self.affinity

    def getID(self):
        return self.id
