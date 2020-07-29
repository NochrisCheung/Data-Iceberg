from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

file = open("sapien_rating","w")

rating_page_url = "https://www.goodreads.com/book/show/23692271-sapiens?from_search=true"
#rating_browser = webdriver.Chrome(rating_page_url)
url = requests.get(rating_page_url)
review_page = BeautifulSoup(url.content, 'html.parser')

book_title = review_page.findAll("h1", attrs={"id":"bookTitle"})
book_title = book_title[0].text.strip()

all_reviews = review_page.findAll("div", attrs={"class": "friendReviews elementListBrown"})
review_date = [review_date.findAll("a", attrs={"class":"reviewDate createdAt right"}) for review_date in all_reviews]
review_date = [date[0].text for date in review_date]
ratings = [ratings.findAll("span", attrs={"class": "staticStars"}) for ratings in all_reviews]

rate_list = []
for rating in ratings:
    stars = rating[0].findAll("span", attrs={"class": "staticStar p10"})
    rate_list = rate_list + [str(len(stars))]

for i in range(0, len(review_date)):
    file.write(review_date[i] + ";")
    file.write(str(rate_list[i]) + "\n")

next_link = review_page.findAll("a", attrs={"class": "next_page"})
print(len(next_link))
next_link = next_link[0].attrs["href"]
print(next_link[0])

#rating_onclick = review_page.findall("a", attrs={"class": "next_page"})
#rating_onclick = rating_onclick.findall["onclick"]
#print(rating_onclick)

#rating_browser.execute_script()

#next_page = review_page.findAll("a", attrs={"class": "next_page"})
#next_page = next_page[0].findAll("href")

#print next_page
file.close()
