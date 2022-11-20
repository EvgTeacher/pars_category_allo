import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


user = fake_useragent.UserAgent().random

headers = {'user-agent': user}

session = requests.Session()

page = int(input('Input page '))
url_input = input('Input URL categories ')
for j in range(1, page+1):
    url = f'{url_input}p-{j}'
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    all_product = soup.find('div', class_='products-layout__container products-layout--grid')
    product_list = all_product.find_all('div', class_='product-card')
    for i in range(len(product_list)):
        product = product_list[i].find('a', class_='product-card__title').text
        url_product = product_list[i].find('a', {"href": "/currencies/bitcoin/markets/"})
        try:
            old_price = product_list[i].find('div', class_='v-pb__old').text
            new_price = product_list[i].find('div', class_='v-pb__cur discount').text
            with open('myproduct.txt', 'a', encoding='UTF-8') as file:
                file.write(f"{product}   Old price  {old_price} New price {new_price}'\n'")
        except AttributeError:
            print('Old price no!')
    print(f"Закончил {j} страницу")
