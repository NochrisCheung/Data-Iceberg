# parse vehicles registration details
from bs4 import BeautifulSoup
from mechanize import Browser

search_url = "https://ovi.rdw.nl/"
automobile_browser = Browser()
resp = automobile_browser.open(search_url)

for i in range(1, 99):
    automobile_browser.select_form(id="aspnetForm")
    automobile_browser["ctl00$TopContent$txtKenteken"] = str(i)+"RXLP"
    resp = automobile_browser.submit()
    page_code = BeautifulSoup(resp.read(), "html5lib")
    car_model = page_code.findAll("div", attrs={"class": "ui-block-a"})
    car_model = car_model[0].find("p")
    car_model = car_model.text.strip()
    print(str(i)+". "+car_model)
