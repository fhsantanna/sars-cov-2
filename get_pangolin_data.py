#/usr/bin/env python

#Author: Dr. Fernando Hayashi Sant'Anna
#Date: 2021-02-18

#This script accesses https://cov-lineages.org/lineages/, captures lineage and its associated metadata.

#Usage: python get_pangolin_data.py <lineage_file> <out_file>

import re
from bs4 import BeautifulSoup
import requests
import sys

lineage_input = sys.argv[1]
outfile_name = sys.argv[2]


outfile = open(outfile_name, "a")
outfile.write("lineage" + "\t" + "countries" + "\t" + "earliest_date" + "\t" + "n_designated" + "\t" + "n_assigned" +
              "\t" + "history" + "\t" + "description" + "\n")

with open(lineage_input) as file:
    lines = file.readlines()
    
    for line in lines:
        line = line.strip('\n') 
        url = "https://cov-lineages.org/lineages/lineage_" + line + ".html"

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
        outfile.write(lineage + "\t" + countries + "\t" + earliest_date + "\t" + n_designated + "\t" + n_assigned +
             "\t" + history + "\t" + description + "\n")

outfile.close()
