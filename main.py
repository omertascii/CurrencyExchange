import requests
import json
import pprint
import pandas as pd

user_input = input("Çevireceğin Para Birimi: ")
base = user_input

user_input2 = input("Hangi Para Biriminine Çevirmek İstiyorsun: ")
out_curr = user_input2

user_input3 = input("Hangi Tarihten İtibaren: ")
start_date = user_input3

user_input4 = input("Hangi Tarihe Kadar: ")
end_date = user_input4

url = 'https://api.exchangerate.host/timeseries?base={0}&start_date={1}&end_date={2}&symbols={3}'.format(base,start_date,end_date,out_curr)
response = requests.get(url)

data = response.json()

rates = []

for i,j in data["rates"].items():
    rates.append([i,j[out_curr]])


df = pd.DataFrame(rates)
df.columns = ["Tarih","Oran"]
print(df)