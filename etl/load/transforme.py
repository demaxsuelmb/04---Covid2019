import pandas as pd

# origen local raw file 
folder_origem = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/04 - Covid2019/data/raw/'
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
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/04 - Covid2019/data/processed/'
output_file = file_name + '_extracted'

# transform in a DataFrame
df = pd.DataFrame(df)

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + output_file + '.csv', mode='a', header=True, index=False)

print("File saved successfully!")