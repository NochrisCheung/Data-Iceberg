from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pds
import os

def parse_wiki_page(wiki_url):
    webpage_request = Request(wiki_url)
    webpage = urlopen(webpage_request).read()
    page_soup = BeautifulSoup(webpage,'html.parser')

    return page_soup

def get_company_name_website(page_soup):
    company_name = page_soup.find('h1',attrs={'id':'firstHeading'}).text
    company_website = page_soup.find('table',attrs={'class': 'infobox vcard'}).find('th',string = 'Website').next_sibling.text

    return [company_name, company_website]

ftse100_list_url = 'https://en.wikipedia.org/wiki/FTSE_100_Index#List_of_FTSE_100_companies'
ftse_soup = parse_wiki_page(ftse100_list_url)
ftse_table = ftse_soup.find('table',attrs={'id':'constituents'})
url_list = ftse_table.select('a[href*=wiki]')

ftse_company_url = pds.DataFrame()
for url in url_list:
    print(url['href'])
    target_wiki_url = 'https://en.wikipedia.org/' + url['href']
    target_soup = parse_wiki_page(target_wiki_url)
    ftse_company_url = ftse_company_url.append([get_company_name_website(target_soup)],ignore_index=True)

ftse_company_url.columns = ['company', 'website']

file_dir = os.path.dirname(os.path.realpath(__file__))
ftse_company_url.to_csv(file_dir+'FTSE100.csv')

company_list = ftse_company_url['company'].to_list()
website_list = ftse_company_url['website'].to_list()
for company, website in zip(company_list, website_list):
    company = company.replace('PLC', '').replace('plc', '')
    print(company, website)
