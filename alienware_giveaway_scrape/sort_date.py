import pandas as pd
import csv

with open('alienwarearena_giveaway_scrape.csv', encoding="utf8", errors='ignore') as f:
    df = pd.read_csv(f, parse_dates=["Date Posted"]) #changes date string to a datetime object
    df.sort_values(['Date Posted'], inplace=True, ascending=False) #rearranges date
    print(df['Date Posted'])

    try:
        df.to_csv('alienwarearena_giveaway_scrape.csv', index=False)
        print('Import success!')
    except Exception as e:
        print('Did not import to csv file!')
