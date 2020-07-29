from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import json
import os
import webbrowser
import re

mydir = '/Users/nochris/Documents/Culture'

def init_glassdoor_url(target_company):
    root_url_prefix = 'https://www.glassdoor.co.uk/Reviews/london-'
    root_url_suffix = '-reviews-SRCH_IL.0,6_IM1035_KE7,'
    url_request_length = str(len(target_company)+ 7)

    return root_url_prefix+target_company+root_url_suffix+url_request_length +'.htm'

def parse_page(parse_url):
    web_request = Request(parse_url, headers={'User-Agent': 'Morzilla/5.0'})
    webpage = urlopen(web_request).read()
    page_soup = BeautifulSoup(webpage,'html.parser')

    return page_soup

def get_company_review_page_url(page_soup, website_url):
    head_cells = page_soup.find_all('div', attrs={'class': 'header cell info'})
    for cell in head_cells:
        if website_url.lower() in cell.find('span',attrs={'class':'webInfo'}).text:
            confirmed_cell = head_cells[head_cells.index(cell)]
            break


    try:
        return confirmed_cell.find('a', attrs={'class':'tightAll h2'})['href']
    except NameError:
        print('Cannot match a cell with the website url')
        return ''

# def scrape_company_search_page(page_soup):
#     container = page_soup.find_all('div', attrs={'class': 'eiHdrModule module snug'})
#     company_info = pd.DataFrame()
#
#     for company in container:
#         try:
#             company_name = company.find_all('a', attrs={'class': 'tightAll h2'})
#             rating = company.find_all('span', attrs={'class': 'bigRating strong margRtSm h1'})
#             review_count = company.find_all('span', attrs={'class': 'num h2'})
#             company_info = company_info.append([[company_name[0].contents[0], rating[0].contents[0], review_count[0].contents[0]]], ignore_index=True)
#         except:
#             print('Something is wrong in the container')
#             continue
#
#     # print(company_info)
#     company_info.columns = ['company_name', 'rating', 'review_count']
#     return company_info

def scrape_company_review_page(page_soup):
    script = page_soup.find('script', attrs={'type': 'application/ld+json'})
    company_info = pd.DataFrame()
    if script == '':
        print('No json script')
        return company_info
    review_page_script = json.loads(script.contents[0])

    try:
        company_name  = review_page_script['name']
        rating  = review_page_script['aggregateRating']['ratingValue']
        review_count = page_soup.find('a', attrs={'class': 'eiCell cell reviews'}).find('span', attrs={'class': 'num h2'})
        if 'k' in review_count.contents[0]:
            print('Review count contains the character K')
            review_number_text = page_soup.find('div',attrs={'class': 'module snug empStatsAndReview'}).find('a', attrs={'class': 'moreBar'}).text
            review_count = re.sub('[^0-9]', '',review_number_text)
        else:
            print('No character K in count review')
            review_count = review_count.contents[0]
        used_review_count = review_page_script['aggregateRating']['ratingCount']
        company_info = company_info.append([[company_name, rating, review_count, used_review_count]],ignore_index=True)
    except:
        print('Something is wrong in the container')

    company_info.columns = ['company_name', 'rating', 'review_count','used_review_count']
    print('Successfully scrape review page')
    return company_info

def filter_correct_company_info(company_info):
    if company_info['review_count'].values == '--':
        print('No review')
        company_info['review_count'] = 0
    else:
        try:
            # factors = company_info['review_count'].replace(r'[k]+$', '', regex=True).astype(float)
            factors = company_info['review_count'].replace('k', '', regex=True).astype(float)
            multipliers = company_info['review_count'].str.extract(r'[\d\.]+([k]+)', expand=False).fillna(1).replace('k', 10**3).astype(int)
            company_info['review_count'] = factors * multipliers
            print('Character K is removed and recalculated')
        except ValueError:
            print('ValueError')

    return company_info
    # return company_info[company_info['review_count'] == company_info['review_count'].max()].drop_duplicates(subset=['review_count'])

def is_search_page(page_soup):
    check_url = page_soup.find_all('link', attrs={'rel': 'canonical'})
    if 'SRCH' in check_url[0]['href']:
        return True
    print('Not a search page')
    return False

def scrape_target_company_info(target_company, website_url):
    parse_url = init_glassdoor_url(target_company)
    page_soup = parse_page(parse_url)
    if is_search_page(page_soup) == True:
        # company_info = scrape_company_search_page(page_soup)
        url_suffix = get_company_review_page_url(page_soup, website_url)
        if url_suffix is '':
            return []
        parse_url = 'https://www.glassdoor.co.uk'+url_suffix
        page_soup = parse_page(parse_url)

    company_info = scrape_company_review_page(page_soup)
    if company_info.empty:
        print('No information scrapped')
        return company_info
    return filter_correct_company_info(company_info)


# ftse_list = pd.read_csv(mydir+'FTSE100.csv')
ftse_list = pd.read_csv(mydir+'/ftse100_rescrape.csv')
company_list = ftse_list['company'].to_list()
website_list = ftse_list['website'].to_list()
#
# company = company_list[2]
# company = company.replace('PLC', '').replace('plc', '').rstrip().replace(' ','-')
# website = website_list[2]
# parse_url = init_glassdoor_url(company)
# webbrowser.open(parse_url)
# print(parse_url)
# page_soup = parse_page(parse_url)
# is_search_page(page_soup)
#
#

target_companies_info = pd.DataFrame()
for company, website in zip(company_list, website_list):
    company = company.replace('PLC', '').replace('plc', '').rstrip().replace(' ','-')
    print(company+':')
    try:
        target_companies_info = target_companies_info.append(scrape_target_company_info(company, website), ignore_index=True)
        print('Succesfully scrape company info from ' +  company) #need to also consider empty list situation
    except:
        print('Skip '+company)

    print('\n')

print(target_companies_info)

target_companies_info[:].to_csv(mydir+'/ftse100_glassdoor_grades_rescraped.csv')
target_companies_info.columns
target_companies_info['rating'].astype(float).median()

parse_url = init_glassdoor_url('Anglo-American')
page_soup = parse_page(parse_url)
print(page_soup.prettify)
# target_company = 'google'
# root_url_prefix = 'https://www.glassdoor.co.uk/Reviews/london-'
# root_url_suffix = '-reviews-SRCH_IL.0,6_IM1035_KE7,'
# url_request_length = str(len(target_company) + 7)
# parse_url = root_url_prefix+target_company+root_url_suffix+url_request_length +'.htm'
# page_soup = parse_page(target_company)
# container = page_soup.find_all('div', attrs={'class': 'sponsoredEmployerOverview'})
# check_url = page_soup.find_all('link', attrs={'rel': 'canonical'})
#
# website_url = 'www.3i.com'
