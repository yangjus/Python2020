from bs4 import BeautifulSoup
import requests
import csv
import re

'''
This scraper finds all World of Tanks giveaways from Alienwarearena
'''
def regex_formatting(unrefined_text): # format text, removing spacing and others
    refined_text = ' '.join(re.split("\s+", unrefined_text, flags=re.UNICODE))
    refined_text_without_beginning_or_end_space = re.sub("^\s+|\s+$", "", refined_text, flags=re.UNICODE)
    return refined_text_without_beginning_or_end_space

source = requests.get('https://na.alienwarearena.com/search/giveaway/World%20of%20Tanks').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('alienwarearena_giveaway_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Date Posted', 'Video Link'])

giveaways = soup.find('div', class_="row no-gutters search-results__grid")

for article in giveaways.find_all('article', class_="col-sm-6 col-md-3")[1:]:

    headline = article.find('div', class_="search-results__item").h1.text
    print(headline)

    paragraph = article.find('div', class_="search-results__item").p.get_text()
    summary = paragraph.split('\n')[1:]
    main_summary = summary.pop(0)
    refined_summary = regex_formatting(main_summary)
    print(refined_summary)

    date = article.find('div', class_="search-results__item").small.text
    refined_date = regex_formatting(date)
    print(refined_date)

    link_id = article.find('a', class_="search-results__wrapper-giveaway")['href']
    link = f'https://na.alienwarearena.com{link_id}'
    print(link)

    print()

    csv_writer.writerow([headline, refined_summary, refined_date, link])

csv_file.close()
