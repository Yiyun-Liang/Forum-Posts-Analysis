#!/usu/bin/python

import sys

old_post = None
count_len = 0.0
count = 0

for line in sys.stdin:
    data = line.strip().split()

    if len(data) != 2:
        continue

    this_post, this_ans = data

    if old_post and old_post != this_post:
        print "{0}\t{1}".format(this_post, count_len/count)
        count_len = 0
        count = 0

    old_post = this_post
    count_len += len(this_ans)
    count += 1

if old_post != None:
    print "{0}\t{1}".format(this_post, count_len/count)
