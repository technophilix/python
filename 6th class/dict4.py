#loop in dictionary

dict = {'Name':"Agniswar", "ID":45, 'Salary': 6000}

for k in dict:
    print(k)


for k in dict:
    print(dict[k])

for k, v in dict.items():
    print("key = {} and value = {}".format(k,v))
