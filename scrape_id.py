from bs4 import BeautifulSoup
import requests
import csv

'''
This scraper finds id for each skin on cs:go stash
'''

'''CSV file'''
csv_file = open('csgo_skin_ids.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Item Type', 'Item Id', 'Item Name'])


'''Setting up source web link'''
which_weapon = {'Pistols': {1: 'CZ75-Auto', 2: 'Desert+Eagle', 3: 'Dual+Berettas',
                            4: 'Five-SeveN', 5: 'Glock-18', 6: 'P2000',
                            7: 'P250', 8: 'R8+Revolver', 9: 'Tec-9', 10: 'USP-S'},
                'Rifles': {1: 'AK-47', 2: 'AUG', 3: 'AWP', 4: 'FAMAS',
                            5: 'G3SG1', 6: 'Galil+AR', 7: 'M4A1-S',
                            8: 'M4A4', 9: 'SCAR-20', 10: 'SG+553', 11: 'SSG+08'},
                'SMGs': {1: 'MAC-10', 2: 'MP5-SD', 3: 'MP7', 4: 'MP9',
                            5: 'PP-Bizon', 6: 'P90', 7: 'UMP-45'},
                'Heavy': {1: 'MAG-7', 2: 'Nova', 3: 'Sawed-Off',
                            4: 'XM1014', 5: 'M249', 6: 'Negev'},
                'Knives': {1: 'Nomad+Knife', 2: 'Skeleton+Knife', 3: 'Survival+Knife',
                            4: 'Paracord+Knife', 5: 'Classic+Knife', 6: 'Bayonet',
                            7: 'Bowie+Knife', 8: 'Butterfly+Knife', 9: 'Falchion+Knife',
                            10: 'Flip+Knife', 11: 'Gut+Knife', 12: 'Huntsman+Knife',
                            13: 'Karambit', 14: 'M9+Bayonet', 15: 'Navaja+Knife',
                            16: 'Shadow+Daggers', 17: 'Stiletto+Knife',
                            18: 'Talon+Knife', 19: 'Ursus+Knife'},
                }
for weapon in which_weapon['Knives'].values():
    source_link = 'https://csgostash.com/weapon/{}'.format(weapon)
    source = requests.get(source_link).text
    source = source.encode('ascii', 'ignore') # ignores the unicode error!
    soup = BeautifulSoup(source, 'lxml')

    print(soup.encode("utf-8"))


    '''Scraping item urls for type, id, and title name'''
    for item in soup.find_all('div', class_='well result-box nomargin'):
        all_links = item.select('a')    # one way to get a href link
        for link in all_links:
            item_link = link['href']
            if link == all_links[2]:    #once loop reaches desired url
                break
        print(item_link)
        '''now extract info from the item link'''
        try:
            item_link = item_link.split('/')
            print(item_link)

            item_type = item_link[-3]
            print(item_type)

            item_id = item_link[-2]
            print(item_id)

            item_name = item_link[-1]
            print(item_name)

            csv_writer.writerow([item_type, item_id, item_name])
        except Exception as e:
            pass

        print()

csv_file.close()
