# 8-Argumento2.py
import sys
# save the arguments
arguments = sys.argv
# get the file path
file_path = arguments[0]
with open(file_path, 'r') as f:
  for line in f:
    print (line)