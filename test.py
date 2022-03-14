import json
from numpy import arange
import pandas as pd
import time

z=[]
with open('z.json','r') as f:
    studentDict = json.load(f)
    z.append(studentDict)      

a=[]
with open('json_data.json','r') as f:
    studentDict = json.load(f)
    a.append(studentDict)


array=[]
for item in z[0]:
    n = item
    if(a[0][n['id']]) :
        n['text'] = a[0][n['id']]
    array.append(n)
    e = json.dumps(array, ensure_ascii=False,indent=4)
    with open('dialect.json', 'w', encoding='utf-8') as file_obj:
        file_obj.write(e)  







      