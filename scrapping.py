from bs4 import BeautifulSoup
import requests, openpyxl
from scrapping import next_page_info

try:
    for page in range(1,51):
        if page == 1:
            url = 'https://books.toscrape.com/'
        else:
            url = 'https://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        source = requests.get(url)
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')
        # Get all list of book details from the page
        all_div = soup.find('div',class_='col-sm-8 col-md-9').find('section').find('div',class_=None)\
        .find('ol',class_='row').find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
except Exception as e:
    print(e)

l,sheet,excel = next_page_info(all_div,url)

# inserting data to excel
for row in l:
    sheet.append(row)
# write data to excel
excel.save('scrap_data.xlsx')
