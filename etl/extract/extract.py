import pandas as pd
import json

# open credencials and configs
with open('config/config.json') as f:
    config = json.load(f)

# Access the configuration values
folders = config['folders']

# origen local raw file 
folder_origem = folders['f_extract']
file_name = 'DADOS_COVID' 

# Connect with csv file
df = pd.read_csv(folder_origem + file_name + '.csv', delimiter=',', header=0, encoding='utf-8')

# filter data without values
df = df.dropna(subset=['city'])

# select columns
df = df[[
          'city_ibge_code'
        , 'date'
        , 'epidemiological_week'
        , 'estimated_population'
        , 'estimated_population_2019'
        , 'is_last'
        , 'is_repeated'
        , 'last_available_confirmed'
        , 'last_available_confirmed_per_100k_inhabitants'
        , 'last_available_date'
        , 'last_available_death_rate'
        , 'last_available_deaths'
        , 'new_confirmed'
        , 'new_deaths']]

# sort values
df = df.sort_values('date', ascending=True)

# Specify the new folder path
output_folder = folders['d_transform']
output_file = file_name + '_extracted'

# transform in a DataFrame
df = pd.DataFrame(df)

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + output_file + '.csv', mode='a', header=True, index=False)


print("File saved successfully!")