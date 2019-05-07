#!/usr/bin/env python3


#Input is via standard input.
#Output is via standard output.


from os import getcwd
from os import listdir
from re import match
from re import search
from re import findall
from sys import stdin
from string import capwords
import csv

file_name_current_search = "artigos.csv"
file_name_data_base = "artigos_base.csv"
file_current_search = open(file_name_current_search)
file_data_base = open(file_name_data_base)

file_result = open("result.csv", "wb")
writer = csv.writer(file_result)

#lines = csv.reader(file)
artigos_current_search = csv.DictReader(file_current_search)

for artigo_current_search in artigos_current_search:
    print("1 - Nome:", artigo_current_search["Document Title"])

    file_data_base = open(file_name_data_base)
    artigos_data_base = csv.DictReader(file_data_base)
    for artigo_data_base in artigos_data_base:
        print("2 - Nome:", artigo_data_base["Document Title"])

        if (artigo_current_search["Document Title"] == artigo_data_base["Document Title"]):  
            print("Combinou")
            writer.writerow([artigo_current_search["Document Title"], artigo_current_search["Authors"], artigo_current_search["Publication_Year"]])
            break
