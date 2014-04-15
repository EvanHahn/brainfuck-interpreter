#!/usr/bin/env python

from re import sub
from sys import argv

if __name__ == "__main__":

    filename = argv[1]

    with open(filename) as file:
        src = file.read()
        print sub(r"[^<>\[\]\+-\.,]", "", src)
