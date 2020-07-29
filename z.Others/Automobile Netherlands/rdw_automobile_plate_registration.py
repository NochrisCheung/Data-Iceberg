# parse vehicles registration details
from bs4 import BeautifulSoup
import requests
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

file = open("vehicle_data.txt", "w")

for i in range(1, 99):
    print(str(i))
    url = requests.get("https://autorapport.finnik.nl/kenteken/"+"4TLZ"+str(i)+"?utm_source=VWE%20Website&utm_medium=VWE%20kentekenbox&utm_campaign=VWE%20kentekenbox")
    page_code = BeautifulSoup(url.content, "html.parser")

    car_model = page_code.findAll("div", attrs={"class": "col-6 spot-head-text"})
    car_model = [model.find("h2") for model in car_model if model is not None]
    if len(car_model) > 0:
        file.write((str(i) + ". " + car_model[0].text).encode("utf8") + "\n")
    else:
        file.write(str(i) + ". " + "\n")
        #car_model = car_model.text.strip()
    #    print(str(i)+". "+car_model)
file.close()
