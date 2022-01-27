import requests
from bs4 import BeautifulSoup
import csv

#make a URL request
page = requests.get("https://worldometers.info/coronavirus/weekly-trends/#weekly_table")
soup = BeautifulSoup(page.content,'html.parser')

#create all data as empty
all_data = []

#extract data
stats = soup.select('table.table')
for statistics in stats:
    Continent = statistics.select('tr.row_continent')[0].text.strip()
    Data = statistics.select('tbody')[0].text.strip()


all_data.append({
      "Continent":Continent,
      "Data":Data
})


keys = all_data[0].keys()

with open('covid19.csv','w', newline='')as output_file:
    dict_writer =csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_data)

