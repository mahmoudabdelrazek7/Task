import json
import csv
import requests
import pandas as pd
import time


url ='https://recruitment.aimtechnologies.co/ai-tasks'


# def  csvConvert(csv_path , json_path):

#     jsonArray = []

#     with open(csv_path , encoding='utf-8') as csvfile:
        
#         csvReader = csv.DictReader(csvfile)

#         for row in csvReader:
#             jsonArray.append(row)
    
#     with open(json_path , 'w', encoding='utf-8') as jsonfile:  
#         jsonfile.write(json.dumps(jsonArray , indent=4))
#     print('Data Convert')

# csv_path = r'dialect_dataset.csv'
# json_path = r'Json.json'

# csvConvert(csv_path , json_path)
 

with open("Json.json") as file:
    db = json.load(file)

items = []
for item in db:
    items.append(item['id'])

x=0
y=1000



for i in range(int(len(items)/1000)):
    res = requests.post(url,json=items[x:y])
    x=x+1000
    y=y+1000
    res = res.json()
    e = json.dumps(res, ensure_ascii=False,indent=4)
    with open('json_data.json', 'a') as file_obj:
        file_obj.write(e)
    time.sleep(1)       


        