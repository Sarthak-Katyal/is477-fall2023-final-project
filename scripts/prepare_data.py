# imports
import requests
import hashlib
import zipfile
import os

# Downloading the Dataset
url = 'https://archive.ics.uci.edu/static/public/53/iris.zip'
response = requests.get(url)

# Creating Correct Subdirectory
if not os.path.exists('data/iris'):
    os.makedirs('data/iris', exist_ok=True)

with open('data/iris/iris.zip', mode='wb') as f:
    f.write(response.content)

# Extracting Zipfile
with zipfile.ZipFile('data/iris/iris.zip', "r") as zip_reference:
    zip_reference.extractall('data/iris')

# Calculating SHA-256 using hashlib for the iris zipfile
filename = 'data/iris/iris.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    iris_sha256 = 'd11fe30213d36434a0879aab7cb00ce3c812eb7ba2495874438abff7b7b762e9'
    if iris_sha256 != sha256hash:
        print("Computed hash does not match expected hash")
    else:
        print("Computed hash matches expected hash")