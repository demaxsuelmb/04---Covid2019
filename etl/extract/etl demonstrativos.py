import pandas as pd

# folder Origin
folder_origin = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/03 - Account_KPIs/data/raw/'
file_name = 'base_demonstracoes.xlsx'


# Connect with Excel file
df = pd.read_excel(
                    folder_origin + file_name
                    , sheet_name='base_demonstracoes'
                    , header=2)

# select columns
df = df[[     'Unnamed: 1'
              , 'Unnamed: 2'
              , 'Unnamed: 3'
              , 'Unnamed: 4'
              , 'Unnamed: 5'
              , 'Unnamed: 6'
              , 'Unnamed: 7'
              , 'Unnamed: 8'
              , 'Unnamed: 9'
              , 'Unnamed: 10'
              , 'Unnamed: 11'
              , 'Unnamed: 12'
              , 'Unnamed: 13']]


df.columns = df.iloc[0]
df = df[1:]

# Unpivot columns using melt
df = df.melt(id_vars='DESCRIÇÃO', var_name='mes_ano', value_name='value')

# rename columns
df = df.rename(columns={   
              'DESCRIÇÃO': 'conta'
              , 'value': 'valor'
               })

# filfiltrar dados sem valor
df = df.dropna(subset=['conta'])

# Specify the new folder path and name of file
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/03 - Account_KPIs/data/processed/'
name_file = 'demostrative_process.csv'

# transform in a DataFrame
df = pd.DataFrame(df)

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + name_file, mode='a', header=True, index=False)

print("File saved successfully!")