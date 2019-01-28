import json,requests
from flask import Flask,request

app = Flask('main')

from req import Req
from map import Map
from search import Search

@app.route('/sendmethod')
def main(city,rank,params,min,max):
    d = Search()
    #params=['Mount Carmel West','Dodge Rec Center','University of British Columbia']
    d.setRanking(rank)
    templist=d.search(city,params,min,max)
    hid=d.bestHouseCandidate(templist)
    #print(hid)
    data = d.findHouseFromID(hid)
    #print(data)
    
    #print(json.loads(data)['long'])



    f=open('data.json','w+')
    f.write(json.dumps(data))

@app.route('/postmethod', methods = ['POST'])
def post_javascript_data():
    jsdata = request.form['data']
    print(jsdata)
    alist = [None]*5

    alist[0] = json.loads(jsdata)['workAddress']
    alist[1] = json.loads(jsdata)['schoolAddress']

    rlist = [None]*5

    rlist[0] = json.loads(jsdata)['workRank']
    rlist[1] = json.loads(jsdata)['schoolRank']

    rlist[1] = ''

    lst = [x for x in alist if x is not '']
    rst = [x for x in rlist if x is not '']

    city = 'Colombus'
    min = 0
    max = json.loads(jsdata)['maxPrice']

    r = requests.post('http://138.197.162.192/front',{'data':'test'})

    main(city,rst,lst,min,max)

    return "OK"

#main('a',['Dodge Rec Center'],0,100000)

Flask.run(app,host="0.0.0.0",port=8080)
