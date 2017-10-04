dict1 = {
    'status': 200,
    'method': 'post',
    'results':[
        {'author':'Bob', 'text':'Hi my name is Bob'},
        {'author':'Frank', 'text':'Hi my name is Frank'},
        {'author':'Tim', 'text':'Hi my name is Tim'},
        {'author':'Mike', 'text':'Hi my name is Mike'},
        {'author':'Jose', 'text':'Hi my name is Jose'},
        {'author':'Jeff', 'text':'Hi my name is Jeff'},
    ]
}


# dict['results'][0]['author'] = "Not Bob"
# dict['results'][1]['text'] = "OMG!!!"

# # 1 - author: txt

# for idx, message in enumerate(dict['results']):
#     print "{} - {}: {}".format(idx, message['author'], message['text'])


# for key in dict:
#     print key


dict2 = {
    'Students': [
        {'first':'Bob', 'last':'Bobbers'},
        {'first':'Frank', 'last':'Frankbers'},
        {'first':'Tim', 'last':'Timbers'},
        {'first':'Mike', 'last':'Mikebers'},
        {'first':'Jose', 'last':'Josebers'},
    ],
    'Instructors': [
        {'first':'Tom', 'last':'Tombers'},
        {'first':'Morcus', 'last':'Morcusbers'},
        {'first':'Eli', 'last':'Elibers'},
        {'first':'Cat', 'last':'Catbers'},
        {'first':'Dog', 'last':'Dogbers'},
    ]
}

for key, people in dict2.items():
    print key
    for idx, person in enumerate(people):
        first = person['first']
        last = person['last']
        pos = idx + 1
        length = len(first+last)
        print "{} - {} {} - {}".format(pos, first, last, length)
