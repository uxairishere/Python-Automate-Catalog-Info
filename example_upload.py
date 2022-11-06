import requests
import glob

# This example shows how a file can be uploaded using
# The Python Requests module

def upload(file, url):
    with open(file, 'rb') as opened:
        requests.post(url, files ={"file": opened})
images = glob.glob('supplier-data/images/*.jpeg')
url = "http://localhost/upload/"

for file in images:
    upload(file,url)
