#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
import fnmatch
import winsound
import re

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


def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)
    tree_walk_list=[]
    for pdffile in find_files(path, '*.pdf'):
        tree_walk_list.append(pdffile)

    tree_walk_list=natural_sort(tree_walk_list)

    for pdffile in tree_walk_list:
        if pdffile == output_filename:
            continue
        print(f"Appending: '{pdffile}'")
        bookmark = os.path.basename(pdffile[:-4])
        merger.append(pdffile, bookmark)
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    # Add more options if you like

    path=input("enter path: ")
    output_filename=input("enter output filename: ")
    dest_output=os.path.join(path,output_filename+".pdf")
    merge(path, dest_output)

    winsound.Beep(800,1000)
    winsound.Beep(500,1000)
    winsound.Beep(700,1000)
    print("DONE")
