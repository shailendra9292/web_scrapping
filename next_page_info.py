from bs4 import BeautifulSoup
import requests, openpyxl

def page_info(all_div,url):
    #print(url)
    l=[]
    for element in all_div:
        row=[]
        next_page_link =  element.find('a').get('href')
        book_name = element.find('img').get('alt')
        #print(next_page_link)
        #print(book_name)
        url_index = url.find('catalogue') + len('catalogue') 
        url = url[:url_index]
        new_url = url +'/'+ next_page_link
        #print(new_url)
        s = requests.get(new_url)  
        soup = BeautifulSoup(s.text, 'html.parser')
        #print(soup.find('table').find_all('tr'))
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