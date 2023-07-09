import pandas as pd
import json

# open credencials and configs
with open('config/config.json') as f:
    config = json.load(f)

# Access the configuration values
folders = config['folders']

# origen local raw file 
folder_origem =  folders['d_transform']
file_name = 'DADOS_COVID_extracted' 

# Connect with csv file
df = pd.read_csv(folder_origem + file_name + '.csv', delimiter=',', header=0, encoding='utf-8')
# Creating a DataFrame Pandas
df = pd.DataFrame(df)

# Specify the new folder path
output_folder = folders['d_transform']
output_file = 'f_covid'

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + output_file + '.csv', mode='a', header=True, index=False)

print("File saved successfully!")