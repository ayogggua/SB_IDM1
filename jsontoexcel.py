import os,json,csv
filepath = r'C:\Users\Administrator\Desktop\a.json'
first_row = []
with open(filepath,'r+') as fs:
    data = json.loads(fs.read())
    l = len(data['phases'])
    for i in data['phases']:
        phasename = i['measurements'].keys()
        first_row.append(list(phasename))
        # first_row.append(i['name'])
        list2 = [x for x in first_row if x]
        # for (b,h) in zip(phasename,range(l)):
        #     outcomedata = data['phases'][h]['measurements'][b]
    print(list2)
    print(phasename)
    # print(phasename)
    # print(outcomedata)
    # print(first_row)
    # print(data.keys())
    # first_row.append(data['phases'][2]['measurements'].keys())
    # print(list2)
