from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.imobiliare.ro/inchirieri-apartamente/cluj-napoca"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="box-anunt_wp")

with open("Apartment.csv", "w", encoding="utf8", newline="") as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Characteristics']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h2', class_="titlu-anunt").text.replace('\n', '')
        location = list.find('div', class_="location_wp").text.replace('\n', '')
        price = list.find('span', class_="pret-mare").text.replace('\n', '')
        characteristics = list.find('div', class_="swiper-wrapper").text.replace('\n', '')

        info = [title, location, price, characteristics]
        thewriter.writerow(info)
