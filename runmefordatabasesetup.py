import pandas as pd
import numpy as np
from sqlalchemy import create_engine
df=pd.read_csv("IN.csv")



engine = create_engine('postgresql://postgres@localhost:5432/testdb')
df.to_sql('pincode', engine)

pq=pd.read_json("map.geojson")
properties=pq["features"]
name_lst=[]
parent_lst=[]
for i in properties:
    name_lst.append(i["properties"]["name"])
    parent_lst.append(i["properties"]["parent"])
qw=pd.DataFrame(name_lst,columns=["name"])
qw["parent"]=parent_lst
cood_lst=[]
for i in properties:
    cood_lst.append(i['geometry']["coordinates"][0])
qw["coordinates"]=cood_lst
qw.to_sql('compute', engine)