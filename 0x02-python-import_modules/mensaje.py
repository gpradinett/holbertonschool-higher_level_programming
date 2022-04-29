#!/usr/bin/python3
import os

n = "#pythoniscool\n"
var = str.encode(n)

os.write(1, var)
