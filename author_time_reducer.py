#!/usr/bin/python

import sys

old_author = None
hours = [0]*24

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    this_author, this_hour = data

    if old_author and old_author != this_author:
        for hour, count in enumerate(hours):
            if count == max(hours):
                print "{0}\t{1}".format(old_author, hour)

        hours = [0]*24

    old_author = this_author
    hours[int(this_hour)] += 1

if old_author != None:
    for hour, count in enumerate(hours):
        if count == max(hours):
            print "{0}\t{1}".format(old_author, hour)
