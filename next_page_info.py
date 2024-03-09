from bs4 import BeautifulSoup
import requests, openpyxl

def next_page_info(all_div,url):
    l=[]
    for element in all_div:
        row=[]
        next_page_link =  element.find('a').get('href')
        book_name = element.find('img').get('alt')
        s = requests.get(url + next_page_link)  
        soup = BeautifulSoup(s.text, 'html.parser')
        table_data = soup.find('table').find_all('tr')

        # Adding column name to excel sheet 
        excel = openpyxl.Workbook()
        sheet = excel.active
        sheet.append(['Book Name']+[t.find('th').text for t in table_data])

        for t in (table_data):
            td = t.find('td').text
            row.append(td)
        l.append([book_name]+row)

    return([l,sheet,excel])