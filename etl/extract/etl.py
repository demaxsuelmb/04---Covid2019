import pandas as pd

# origen
folder_origem = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/03 - Account_KPIs/data/raw/'
file_name = 'data_hort.csv'

# Connect with csv file
df = pd.read_csv(folder_origem+file_name, delimiter=';', header=6)
df_1 = pd.read_csv(folder_origem+file_name, delimiter=';', header=0)

# extract data
df_data =  df_1.iloc[1,6]
# extract cnpj
df_cnpj =  df_1.iloc[0,6]

# merge column in dataframe
df['cnpj'] = df_cnpj
df['data'] = df_data


df = df[[
         'data'
         , 'cnpj'
         , 'Código'
         , 'Classificação'
         , 'Descrição da conta'
         , 'Unnamed: 9'
         , 'Unnamed: 10'
         , 'Unnamed: 11'
         , 'Saldo Atual'
         ]]


# rename columns
df = df.rename(columns={   
              'Código': 'codigo'
              , 'Classificação': 'classificacao'
              , 'Descrição da conta': 'conta'
              , 'Unnamed: 9': 'sintetica'
              , 'Unnamed: 10': 'sintetica_2'
              , 'Unnamed: 11': 'analitica'
              , 'Saldo Atual': 'valor'
        })

# filtrar dados sem valor
df = df.dropna(subset=['classificacao'])

# Columns_list is a list of column names you want to fill down
columns_list = ['conta', 'sintetica', 'sintetica_2']

# Iterate over each column in the list and fill down the data
for column in columns_list:
    df[column] = df[column].fillna(method='ffill')


# remove nulls
df = df.dropna(subset=['analitica'])

# Extract data before the delimiter into a new column
df['data'] = df['data'].str.split(' -').str[0]

# Specify the new folder path
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/03 - Account_KPIs/data/processed/'

# transform in a DataFrame
df = pd.DataFrame(df)

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'process_data.csv', mode='a', header=True, index=False)

print("File saved successfully!")