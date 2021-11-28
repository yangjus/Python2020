'''
This python file will help organize and sort csgo_skin_ids.csv
'''
import pandas as pd
import numpy as np # for np.nan
import csv

df = pd.read_csv('csgo_skins.csv')

'''Sort by price descending'''
llp = 'Lowest Listing Price ($)'
df[llp] = df[llp].str.replace('$', '')
# next three lines of code makes sure 'No Recent Price' rows go to bottom of df
df = df.replace('No Recent Price', np.nan)
df[llp] = pd.to_numeric(df[llp], errors='coerce')
df.sort_values([llp], inplace=True, ascending=False, na_position='last')
df = df.fillna('No Recent Price')

'''Sort by exterior'''
exterior_order = ['Factory New', 'Minimal Wear',
                'Field-Tested', 'Well-Worn', 'Battle-Scarred']
df.reindex(exterior_order)


'''Import sorted dataframe into csv file'''
try:
    df.to_csv('csgo_skins_sorted.csv', index=False)
    print('Import success!')
except Exception as e:
    print('Could not import to csv file!')
