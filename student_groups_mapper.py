# We might want to help students form study groups.
# But first we want to see if there are already students on forums that
# communicate a lot between themselves.

# As the first step for this analysis we have been tasked with
# writing a mapreduce program that for each forum thread
# (that is a question node with all it's answers and comments)
# would give us a list of students that have posted there - either asked the question,
# answered a question or added a comment. If a student posted to that thread several times,
# they should be added to that list several times as well,
# to indicate intensity of communication.

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
        node_id = line[0]
        author_id = line[3]
        type = line[5]
        parent_id = str(line[7])

        if type == "question":
            print "{0}\t{1}".format(node_id, author_id)

        if type == "answer":
            print "{0}\t{1}".format(parent_id, author_id)
