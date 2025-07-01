import json
with(open('stuff.json', 'r')) as stuff_json:
    file = json.load(stuff_json)
    
file = [
    {
       'name' : "Edward",
       'age' : 14,
       'birthday' : {
           "month" : 7,
           "day" : 27,
           "year" : 2010
       } 
    },
    {
       'name' : "Katherine",
       'age' : 19,
       'birthday' : {
           "month" : 6,
           "day" : 11,
           "year" : 2006
       } 
    },
]

with(open('stuff.json', 'w')) as stuff_json:
    json.dump(file, stuff_json)