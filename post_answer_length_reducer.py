#!/usr/bin/python

import sys

old_post_id = None
old_post_len = None
count_len = 0.0
count = 0

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 3:
        continue

    this_post_id, this_post_len, this_ans_len = data

    if old_post_id and old_post_id != this_post_id:
        print "{0}\t{1}\t{2}".format(this_post_id, this_post_len, count_len/float(count))
        count_len = 0
        count = 0

    old_post_id = this_post_id
    old_post_len = this_post_len
    count_len += int(this_ans_len)
    count += 1

if old_post_id != None:
    print "{0}\t{1}\t{2}".format(this_post_id, this_post_len, count_len/float(count))
