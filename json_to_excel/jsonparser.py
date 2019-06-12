import os,json,csv
outcome_list = []
key_list_temp = []
phasename = []
with open(r'C:\Users\Administrator\Desktop\baromag.json','r+') as fs:
    fs_r = fs.read()
    data = json.loads(fs_r)
    phasedata_temp = data['phases']
    #clear voild list
    phasedata = [x for x in phasedata_temp if x]
    print(len(phasedata))
    for a in phasedata:
        key_values = list(a['measurements'].keys())
        key_list_temp.append(key_values)
        #clear voild list
        key_list = [x for x in key_list_temp if x]

    print(len(key_list))
    key_list_f = [h for m in key_list for h in m]
    for i,j in zip(range(len(phasedata)),key_list):
        for l in j:
            outcome_data = phasedata[i]['measurements'][l]['measured_value']
            outcome_list.append(outcome_data)
    print(key_list)
    print(outcome_list)
first_row = [x for i in key_list for x in i]
with open('result.csv','w', newline = '') as result:
    result_write = csv.writer(result)
    result_write.writerow(first_row)
    result_write.writerow(outcome_list)
    print(' ok  !')

