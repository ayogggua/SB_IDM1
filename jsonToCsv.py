# author:温志超
import os
import json
import time
import csv


def main():
    filenames = []
    outcome_list = []
    key_list_temp = []
    # 输入json所在目录
    filepath = (r'C:\Users\Administrator\Desktop\json_to_excel')
    for i in os.listdir(filepath):
        if not i.endswith('.json'):
            continue
        filenames.append(i)
    print(filenames)
    csvname = time.strftime("%m-%d", time.localtime(int(time.time())))
    with open('log' + csvname + '.csv', 'w+', newline='') as result:
        result_write = csv.writer(result)
        for filename, m in zip(filenames, range(len(filenames))):
            print(filename)
            with open(filename, 'r') as fs:
                json_data = fs.read()
                data = json.loads(json_data)
                cycletime_temp = int(data['end_time_millis']) - int(data['start_time_millis'])
                cycletime = time.strftime('%S',time.localtime(cycletime_temp))
                # print(time_trans(data['start_time_millis']))
                other_keys = ['dut_id', 'station_id', 'outcome', 'test_mode', 'slot', 'start_time_millis', 'end_time_millis', 'cycletime']
                other_items = [data['dut_id'], data['station_id'], data['outcome'], data['test_mode'], data['slot'],
                               time_trans(data['start_time_millis']), time_trans(data['end_time_millis']), cycletime]
                phasedata_temp = data['phases']
                # phasedata = [x for x in phasedata_temp if x]
                # print(len(phasedata_temp))
                for a in phasedata_temp:
                    key_values = list(a['measurements'].keys())
                    key_list_temp.append(key_values)
                    # clear void list
                    # key_list = [x for x in key_list_temp if x]

                # print(len(key_list_temp))
                for i, j in zip(range(len(phasedata_temp)), key_list_temp):
                    for l in j:
                        outcome_data = phasedata_temp[i]['measurements'][l]['measured_value']
                        outcome_list.append(outcome_data)
                # print(outcome_list)
                if m == 0:
                    first_row = [x for i in key_list_temp for x in i]
                    result_write.writerow(other_keys + first_row)
                result_write.writerow(other_items + outcome_list)
                outcome_list = []
                key_list_temp = []
                # result.close()
        print('OK!!')


def time_trans(timedata):
    if len(str(int(timedata))) == 10:
        timeStamp = float(timedata)
    else:
        timeStamp = float(timedata) / 1000
    timeArray = time.localtime(timeStamp)
    timestyle = time.strftime("%y-%m-%d,%H:%M:%S", timeArray)
    return timestyle


if __name__ == '__main__':
    main()

