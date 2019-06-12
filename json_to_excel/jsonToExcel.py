import os,json,csv
# import pysnooper
# @pysnooper.snoop()
def main():
    filenames = []
    outcome_list = []
    key_list_temp = []
    phasename = []
    filepath = (r'C:\Users\Administrator\Desktop\json_to_excel')
    for i in os.listdir(filepath):
        if not i.endswith('.json'):
            continue
        filenames.append(i)
    print(filenames)
    with open('gua.csv','w+', newline = '') as result:
        result_write = csv.writer(result)
        for filename,m in zip(filenames,range(len(filenames))):
            print(filename)
            with open(filename,'r') as fs:
                    json_data = fs.read()
                    data = json.loads(json_data)
                    phasedata_temp = data['phases']
                    # phasedata = [x for x in phasedata_temp if x]
                    print(len(phasedata_temp))
                    for a in phasedata_temp:
                        key_values = list(a['measurements'].keys())
                        key_list_temp.append(key_values)
                        #clear void list
                        # key_list = [x for x in key_list_temp if x]

                    print(len(key_list_temp))
                    for i,j in zip(range(len(phasedata_temp)),key_list_temp):
                        for l in j:
                            outcome_data = phasedata_temp[i]['measurements'][l]['measured_value']
                            outcome_list.append(outcome_data)
                    # print(outcome_list)
                    if m == 0:
                        first_row = [x for i in key_list_temp for x in i]
                        result_write.writerow(first_row)
                    result_write.writerow(outcome_list)
                    outcome_list = []
                    key_list_temp = []
                            # result.close()
                    print(' ok  !')



if __name__ == '__main__' :
    main()