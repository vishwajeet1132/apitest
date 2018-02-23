from flask import Flask, url_for
from flask import request
from flask import json
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
from shapely.geometry import MultiPoint,Point
import psycopg2

hostname = 'localhost'
username = 'postgres'
database = 'testdb'
myConnection = psycopg2.connect( host=hostname, user=username, dbname=database )
app = Flask(__name__)

@app.route('/post_location', methods=['POST'])
def post_location():
    if request.headers['Content-Type'] == 'text/plain':
        text=str(request.data).replace("b'",'')
        lat,long,pin,place,ad=text.split("+")
        cur=myConnection.cursor()
        cur.execute("select key from pincode where key= {0} ".format("\'"+pin+"\'"))
        if cur.rowcount>0:
            return "sorry already present"
        else:
            cur.execute("insert into pincode (admin_name1,latitude,longitude,key,place_name) values (%s, %s, %s, %s, %s)",(ad,lat,long,pin,place))
            myConnection.commit()
            return "the location has been added" + str(request.data).replace("b'",'')
    else:
        return "415 Unsupported Media Type ;)"
	
@app.route('/get_using_postgres', methods=['GET','POST'])
def get_using_postgres():
    if request.headers['Content-Type'] == 'text/plain':
        text=str(request.data).replace("\'",'').replace("b",'')
        lat,long,radius=text.split("+")
        cur=myConnection.cursor()
        query="select place_name from pincode where earth_box(ll_to_earth("+lat+","+long+"), "+radius+") @> ll_to_earth(pincode.latitude, pincode.longitude)"
        cur.execute(query)
        lst=[]
        for a in cur.fetchall():
            lst.append(a)
        return "the places near the point in  given radius are " + str(lst)
    else:
        return "415 Unsupported Media Type ;)"
		
@app.route('/get_using_self', methods=['GET','POST'])
def get_using_self():
    if request.headers['Content-Type'] == 'text/plain':
        query="select place_name,latitude,longitude from pincode"
        cur=myConnection.cursor()
        cur.execute(query)
        text=str(request.data).replace("\'",'').replace("b",'')
        lat,long,dis=text.split("+")
        lst=[]
        for a,b,c in cur.fetchall():
            plc=a
            lat1=radians(float(lat))
            lon1=radians(float(long))
            if b is not None:
                lat2=radians(float(b))
            if b is not None:
                lon2=radians(float(c))
            rad=float(dis)
            R = 6373.0
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c * 1000
            if distance<=rad:
                lst.append(plc)
        return "the places near the point in  given radius are " + str(lst)
    else:
        return "415 Unsupported Media Type ;)"

@app.route('/get_city_name', methods=['GET','POST'])
def get_city_name():
    if request.headers['Content-Type'] == 'text/plain':
        text=str(request.data).replace("\'",'').replace("b",'')
        lat,long=text.split("+")
        cur=myConnection.cursor()
        query="select name,parent,coordinates from compute"
        cur.execute(query)
        sd=pd.DataFrame(cur.fetchall(),columns=["name","parent","coordinates"])
        for index in sd.iterrows():
            kj=sd.coordinates[index[0]].replace("{","").replace("}","").split(",")
            xs=[]
            ys=[]
            c=0
            for i in kj:
                p=float(i)
                if c%2==0:
                    xs.append(p)
                else:
                    ys.append(p)
                c+=1
            sd.coordinates[index[0]]=list(zip(xs,ys))
        x=float(lat)
        y=float(long)
        for index, row in sd.iterrows():
            poly = MultiPoint(row["coordinates"]).convex_hull
            point = Point(y,x)
            if poly.contains(point)==True:
                print(str(sd.loc[index,"name"]))
                return "the place of location is " + str(sd.loc[index,"name"])
    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run(debug=True)
	
	
	
