import json

def json_update(amount, date,util_type):
    util = open('utilities.json', 'r')
    re_util = json.load(util)
    
    re_util[util_type][0]["Date"].append(date)
    re_util[util_type][0]["Amount"].append(amount)
    
    util = open('utilities.json', 'w')
    util.write(json.dumps(re_util))
    util.close()
