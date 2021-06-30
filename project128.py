from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(START_URL)

print(page)
soup = BeautifulSoup(page.text,'html.parser')
star_table=soup.find('table')

temp_list=[]
table_rows = star_table.find_all('tr')
for tr in table_rows :
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)

sname = []
distance = []
mass = []
radii = []


for i in range(1,len(temp_list)):
    sname.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    radii.append(temp_list[i][6])
    mass.append(temp_list[i][5])
    

df2 = pd.DataFrame(list(zip(sname,distance,mass,radii)),columns=['sname','distance','mass','radii'])
df2.to_csv('dwarf.csv')    