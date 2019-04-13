import argparse
from os import listdir
from os.path import isfile
import os

parser = argparse.ArgumentParser(description="Project root directory from where to count")
parser.add_argument('--dir', help="Path of the root")

args = parser.parse_args()

count = 0

    
def count_lines(current_path):
    global count
    list_dir = listdir(current_path)
    for a in list_dir:
        current = current_path +"/" + a
     
        if isfile(current) and current.endswith("py"):
            file = open(current, 'r')
            count = count + len(file.readlines())
            file.close()
            print current

project_path = args.dir
directories = [x[0] for x in os.walk(project_path)]

for directorie in directories:
    count_lines(directorie)

print "\n"
print "{} Rows of Python code".format(count)

