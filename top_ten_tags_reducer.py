#!/usr/bin/python

import sys, string

count = 0
old_tag = None
popular_tags = []

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 1:
        continue

    this_tag = data

    if old_tag and old_tag != this_tag:
        popular_tags.append([count, old_tag])
        count = 0

    old_tag = this_tag
    count += 1

topTen = sorted(popular_tags, reverse=True)[0:10]

for top in topTen:
    print "{0}\t{1}".format(top[1], top[0])
