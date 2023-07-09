import pandas as pd
import json

# open credencials and configs
with open('config/config.json') as f:
    config = json.load(f)

# Access the configuration values
folders = config['folders']

# Connect with csv file
df = pd.read_csv('https://raw.githubusercontent.com/demaxsuelmb/01---Brazilian-Population-Growth/main/cidades_ibge.csv', delimiter=',', header=0, encoding='utf-8')
# Creating a DataFrame Pandas
df = pd.DataFrame(df)

# select columns
df = df[[
             'codibge'
           , 'municipio'
           , 'mesorregiao'
           ,'estado']]

# Specify the new folder path
output_folder = folders['d_transform']
output_file = 'd_cities'

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + output_file + '.csv',  header=True, index=False)

print("File saved successfully!")