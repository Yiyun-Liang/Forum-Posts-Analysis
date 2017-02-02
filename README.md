# Forum-Posts-Analysis

+ For each student what is the hour during which the student has posted the most posts]


### Dataset format

+ "id": id of the node
+ "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
+ "tagnames": space separated list of tags
+ "author_id": id of the author
+ "body": content of the post
+ "node_type": type of the node, either "question", "answer" or "comment"
+ "parent_id": node under which the post is located, will be empty for "questions"
+ "abs_parent_id": top node where the post is located
+ "added_at": date added
