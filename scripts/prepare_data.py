# imports
import requests
import hashlib
import os

# Downloading Data with requests for Adult.zip
original_url = 'https://archive.ics.uci.edu/static/public/53/iris.zip'
original_response = requests.get(original_url)

# Creating correct subdirectory
if not os.path.exists('data'):
    os.makedirs('data', exist_ok=True)

with open('Data/adult/adult.zip', mode='wb') as f:
    f.write(original_response.content)

# Calculating SHA-256 using hashlib for Adult.zip
filename = 'Data/adult/adult.zip'

with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    adult_sha256 = '7537312dd56c2b98035880805ce99e68183a30ee468aa5329d6df0fbb3cc21bb'
    if adult_sha256 != sha256hash:
        print("Computed hash does not match expected hash")
    else:
        print("Computed hash matches expected hash")

# Downloading Data with requests for the reconstructed file
reconstructed_url = 'https://github.com/socialfoundations/folktables/raw/731b8d1470d36bbc1821e1953ba1308303eef95f/adult_reconstruction.csv'
reconstructed_response = requests.get(reconstructed_url)

# Creating correct subdirectory
if not os.path.exists('Data/folktables'):
    os.makedirs('Data/folktables', exist_ok=True)

with open('Data/folktables/adult_reconstruction.csv', mode='wb') as f:
    f.write(reconstructed_response.content)

# Calculating SHA-256 using hashlib for the reconstructed file
filename_2 = 'Data/folktables/adult_reconstruction.csv'

with open(filename_2, mode='rb') as f:
    data = f.read()
    sha256hash_2 = hashlib.sha256(data).hexdigest()
    reconstructed_sha256 = '4895fd481e7ae6e2ca423e6213454b39f0f7ec0efcd741ad2f6c667554f0eb51'
    if reconstructed_sha256 != sha256hash_2:
        print("Computed hash does not match expected hash")
    else:
        print("Computed hash matches expected hash")