#!/usr/bin/python

import sys

old_post = None
participant_id = []

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    this_post, this_author = data

    if old_post and old_post != this_post:
        print "{0}\t{1}".format(old_post, participant_id)
        participant_id = []

    old_post = this_post
    participant_id.append(this_author)

if old_post != None:
    print "{0}\t{1}".format(old_post, participant_id)
