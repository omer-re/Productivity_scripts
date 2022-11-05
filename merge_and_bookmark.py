#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger, PdfFileReader, utils
import os
import fnmatch
import winsound
import re
import operator
import pandas as pd
pd.set_option('display.max_rows', None)

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def sort_hw_num_then_dir(list_of_paths):
    list_of_dicts=[]
    for file_path in list_of_paths:
        full_path=file_path
        last_dir=file_path.split("\\")[-2]
        file_name=os.path.basename(file_path).split(".")[0]
        
        hw_number=get_hw_number(file_name)
        file_dict={"full_path":full_path, "last_dir":last_dir, "file_name":file_name, "hw_number":hw_number}
        list_of_dicts.append(file_dict)
        
    sorted_list_of_dicts=sorted(list_of_dicts, key=operator.itemgetter('hw_number', 'last_dir'))
    print(pd.DataFrame(sorted_list_of_dicts))
    sorted_list_of_dicts_paths=[d['full_path'] for d in sorted_list_of_dicts if 'full_path' in d]
    return sorted_list_of_dicts_paths

def get_hw_number(file_name):
    
    p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'
    if re.search(p, file_name) is not None:
        for catch in re.finditer(p, file_name):
            if catch[0]:
                print (catch[0])
                if int(catch[0])<30:
                    if int(catch[0])<10:
                        return str("0"+catch[0])
                    return catch[0] # catch is a match object
            


def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)
    tree_walk_list=[]
    for pdffile in find_files(path, '*.pdf'):
        tree_walk_list.append(pdffile)

    #tree_walk_list=natural_sort(tree_walk_list)
    
    tree_walk_list=sort_hw_num_then_dir(tree_walk_list)    
    
    for pdffile in tree_walk_list:
        try:
            
            if pdffile == output_filename:
                continue
            else:
                print(f"Appending: '{pdffile}'")
                bookmark = os.path.basename(pdffile[:-4])
                merger.append(pdffile, bookmark)
        except (NotImplementedError, utils.PdfReadError):
            
            print("##  problem with ",pdffile, " dropping it")
            #with open(pdffile, mode='rb') as f:        
            #    reader = PdfFileReader(f)
            #    if reader.isEncrypted:
            #        print(pdffile, " is encrypted, skipping")
            #        continue
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    # Add more options if you like

    path=input("enter path: (leave empty for current working folder)")
    if len(path)<2:
        path= os.getcwd()
    output_filename=input("enter output filename: (leave empty for default name)")
    if len(output_filename)<2:
        output_filename= ''.join("merged_",os.path.split(path)[1])
    dest_output=os.path.join(path,output_filename+".pdf")
    merge(path, dest_output)

    winsound.Beep(800,1000)
    winsound.Beep(500,1000)
    winsound.Beep(700,1000)
    print("DONE")
