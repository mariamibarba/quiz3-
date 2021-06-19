import requests

lat=35.67
lon=22.13
part='hourly'
key='4f68fbf1843d0a8578ba43d49ff3ff02'
url=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}'
r= requests.get(url)
print(r.text)
print(r.status_code)
print(r.headers['Content-Type'])
print(r.content)

import requests
import json
key='4f68fbf1843d0a8578ba43d49ff3ff02'
lat=10.0
lon=55.2
part='hourly'
payload={'appid': key, "lat" :lat, "lon":lon, "part":part }
r=requests.get('https://api.openweathermap.org/data/2.5/onecall?', params=payload)
res=json.loads(r.text)
print(json.dumps(res, indent=3))

import requests
import json
import sqlite3

conn = sqlite3.connect('weather_db.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather
          ( 
           min FLOAT ,
           temp FLOAT 

           ) ''')

lat = 24.45
lon = 34.19
part = 'hourly'
key = '4f68fbf1843d0a8578ba43d49ff3ff02'
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}'
r = requests.get(url)
res = json.loads(r.text)
print(json.dumps(res, indent=3))
print('temperature:', res['current']['temp'])
print('pressure:', res['current']['pressure'])
print('humidity:', res['current']['humidity'])
print('max temperature:', res['daily'][0]['temp']['max'])

with open('weatherapi.json', 'w') as file:
    json.dump(res, file, indent=3)

all_rows = []
for each in res['daily']:
    temp = each['temp']['night']
    min = each['temp']['min']
    row = (temp, min)
    all_rows.append(row)

    # print(temp)
    # print(min)

c.executemany('INSERT INTO weather(temp, min) VALUES (?, ?)', all_rows)
conn.commit()
conn.close()