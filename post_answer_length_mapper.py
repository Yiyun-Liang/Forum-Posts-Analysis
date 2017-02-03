#!/usu/bin/python

import sys
import csv
import string

reader = csv.reader(sys.stdin, delimiter='\t')
# skip the header in the input file
reader.next()

questions = {}
answers = {}

for line in reader:
    # forum node from forum posts dataset
    if len(line) == 19:
        node_id = line[0]
        post = line[4]
        type = line[5]
        post_len = len(post)
        parent_id = str(line[7])

        if type == "question":
            questions[node_id] = post_len

        if type == "answer":
            if not parent_id in answers:
                answers[parent_id] = [post_len]
            else:
                answers[parent_id].append(post_len)

# print format: question_id, question_length, answer_length
for q in questions:
    if q in answers:
        for ans_len in answers[q]:
            print "{0}\t{1}\t{2}".format(int(q), int(questions[q]), ans_len)
    else:
        print "{0}\t{1}\t{2}".format(int(q), int(questions[q]), "0")
