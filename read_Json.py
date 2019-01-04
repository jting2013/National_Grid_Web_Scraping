import json


util = open('job.json', 'r')
re_util = json.load(util)
util.close()


for re_u in re_util:
    print(re_u)

