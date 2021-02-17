#/usr/bin/env python

#Author: Dr. Fernando Hayashi Sant'Anna
#Date: 2021-02-17

#This script accesses https://cov-lineages.org/lineages/, captures lineage and its associated metadata.

#Usage: python get_pangolin_data.py <lineage>

import re
from bs4 import BeautifulSoup
import requests
import sys

lineage = sys.argv[1]
#outfile_name = sys.argv[2]

url = "https://cov-lineages.org/lineages/lineage_" + lineage + ".html"

#outfile = open(outfile_name, "a")

page_url = requests.get(url)
soup = BeautifulSoup(page_url.content, 'html.parser')

table = soup.find('table', id='myTable')

rows = table.find_all('td')[0:7]
lineage = rows[0].get_text()
countries = rows[1].get_text()
earliest_date = rows[2].get_text()
n_designated = rows[3].get_text()
n_assigned = rows[4].get_text()
history = rows[5].get_text()
description =rows[6].get_text()

#outfile.write("lineage" + "\t" + "countries" + "\t" + "earliest_date" + "\t" + "n_designated" + "\t" + "n_assigned" +
#              "\t" + "history" + "\t" + "description" + "\n")
#outfile.write(lineage + "\t" + countries + "\t" + earliest_date + "\t" + n_designated + "\t" + n_assigned +
#              "\t" + history + "\t" + description + "\n")

#outfile.close()

print("lineage" + "\t" + "countries" + "\t" + "earliest_date" + "\t" + "n_designated" + "\t" + "n_assigned" +
              "\t" + "history" + "\t" + "description" + "\n")
print(lineage + "\t" + countries + "\t" + earliest_date + "\t" + n_designated + "\t" + n_assigned +
             "\t" + history + "\t" + description + "\n")