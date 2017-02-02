#!/usu/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
# skip the header in the input file
reader.next()

for line in reader:
    # forum node from forum posts dataset
    if len(line) == 19:
        author_id = line[3]

        # timestamp format: 2012-02-25 08:09:06.787181+00
        # should return '08'
        hour = int(line[8][11:13])
        print "{0}\t{1}".format(author_id, hour)
