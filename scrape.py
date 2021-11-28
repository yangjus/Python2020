from bs4 import BeautifulSoup
import requests
import csv
import re
import pandas as pd

'''
This scraper finds listings for the recent selling price of csgo skins
'''

'''CSV file'''
csv_file = open('csgo_skins.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Item Category', 'Item Name', 'Item Quality', 'StatTrak?',
            'Souvenir?', 'Item Exterior', 'Lowest Listing Price ($)', 'Steam Market Link'])


'''Making multiple url requests'''
df = pd.read_csv('csgo_skin_ids.csv')
print(df.head())
print()

for index, row in df.iterrows():
    type = row['Item Type']
    id = row['Item Id']
    name = row['Item Name']
    #print(type, id, name)
    #print()


    '''Setting up source web link'''
    source_link = 'https://csgostash.com/{}/{}/{}'.format(type, id, name)
    source = requests.get(source_link).text
    source = source.encode('ascii', 'ignore') # ignores the unicode error!
    soup = BeautifulSoup(source, 'lxml')

    #print(soup.encode("utf-8"))


    '''Scraping for item name and quality'''
    item_title = soup.find("div", class_="well result-box nomargin").h2.text
    #print(item_title)

    print('--------------------')
    item_category = item_title.split(" | ")[0]
    print(item_category)

    item_name = item_title.split(" | ")[1]
    if item_name[-1] == ')': #removes the ( )
        item_name = item_name[2:-1]
    print(item_name)

    item_quality_unrefined = soup.find("p", class_="nomargin").text
    item_quality = re.sub(r"\s+$", "", item_quality_unrefined, flags=re.UNICODE)
    print(item_quality)
    print('--------------------')

    '''Scraping for item's stattrak, souvenir, exterior, price, market-link'''
    item_listing = soup.find("div", class_="tab-pane active")
    for item in item_listing.find_all("div", class_="btn-group-sm btn-group-justified"):
        try:
            item_info = item.find('a', href=True).get_text()
            item_info_list = item_info.split('\n')[1:-1]
        except Exception as e:
            pass

        print(item_info_list)

        item_stattrak = True
        if (item_info_list[0] != 'StatTrak'):
            item_stattrak = False
        print(item_stattrak)

        item_souvenir = True
        if (item_info_list[0] != 'Souvenir'):
            item_souvenir = False
        print(item_souvenir)

        item_exterior = item_info_list[-2]
        print(item_exterior)

        item_price = item_info_list[-1]
        print(item_price)
        print()

        try:
            all_links = item.select('a')    #one way to get a href link
            for link in all_links:
                item_link = link['href']
        except Exception as e:
            item_link = 'Not available'

        #print(item_link)
        print()
        if (item_link != 'Not available'):
            csv_writer.writerow([item_category, item_name, item_quality, item_stattrak,
                            item_souvenir, item_exterior, item_price, item_link])

csv_file.close()
