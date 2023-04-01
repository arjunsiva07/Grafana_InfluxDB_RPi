import pandas as pd  
from influxdb import InfluxDBClient

client= InfluxDBClient (host= "localhost",port=8086)
client.switch_database("test")

df=pd.read_csv("stock30.5.csv")
df.dropna(inplace=True)
print (df.shape)

for rwo_pk, row in df.iloc[1:].iterrows():

 json_body=[{
 "measurement": "CovidMap",
 "tags": {"Item":row[0]},
 "fields": {
 "name":row[0],
 "Group":row[1],
 "Min.Quantity":row[2],
 "STOCK":row[3],
 
 }
 }]
 client.write_points(json_body)
 print("done")


          