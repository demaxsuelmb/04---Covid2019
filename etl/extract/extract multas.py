import pandas as pd
from pymongo import MongoClient
import json

# open credencials and configs
with open('config/config.json') as f:
    config = json.load(f)

# Access the configuration values
database = config['mongoDB']
folders = config['folders']

# Credencials to access to database
host = database['host'] 
nome_banco = database['nome_banco'] 
username = database['username'] 
password = database['password'] 

# Conectando ao banco de dados
uri = f"mongodb+srv://{username}:{password}@{host}/{nome_banco}?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client[nome_banco]

# Retrieving data from a collection
collection = db["multas"]
data = list(collection.find())

# Creating a DataFrame Pandas
df = pd.DataFrame(data)

# Specify the new folder path
output_folder = folders['d_transform']
output_file = 'multas_extracted'

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + output_file + '.csv',  header=True, index=False)

print("File saved successfully!")