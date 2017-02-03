#!/usr/bin/python

import sys
import csv
import string

reader = csv.reader(sys.stdin, delimiter='\t')
# skip the header in the input file
reader.next()

for line in reader:
    # forum node from forum posts dataset
    if len(line) == 19:
        type = line[5]
        if type == "question":
            tags = line[2]
            tag_names = tags.split()
            for tag in tag_names:
                print "{0}".format(tag)
