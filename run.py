
from os import listdir, path
import requests
import json
import glob

texts = glob.glob('supplier-data/descriptions/*.txt')
images = glob.glob('supplier-data/images/*.jpeg')

# texts = os.listdir('supplier-data/descriptions')

feedback = []

def getData(file):
    
    # storing text file data 
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name, weight, description = lines
    
    # getting images name 
    entry_id = path.splitext(path.basename(file))[0]
    img_name = entry_id + ".jpeg"
    
    # format to integer 
    weight = int(weight.replace("lbs", ""))
    
    # entring data in json  
    keys = ["name", "weight", "description", "image_name"]
    vals = [name, weight, description, img_name]
    
    entering_data = dict(zip(keys, vals))
    
    return entering_data
    
url = "http://localhost/fruits/"

for file in texts:
    data = getData(file)
    res = requests.post(url, data=data)
    if res.ok:
        print("success")
    else:
        print(f"error: {res.status_code}")