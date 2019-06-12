# author:温志超
import os, json, csv


def main():
    filenames = []
    outcome_list = []
    key_list_temp = []
    filepath = (r'C:\Users\Administrator\Desktop\json_to_excel\1')
    for i in os.listdir(filepath):
        if not i.endswith('.json'):
            continue
        filenames.append(i)
    print(filenames)
    with open('result.csv', 'w+', newline='') as result:
        result_write = csv.writer(result)
        for filename, m in zip(filenames, range(len(filenames))):
            print(filename)
            with open(filename, 'r') as fs:
                json_data = fs.read()
                data = json.loads(json_data)
                other_keys = ['dut_id', 'station_id', 'outcome', 'test_mode', 'slot', 'start_time_millis']
                other_items = [data['dut_id'], data['station_id'], data['outcome'], data['test_mode'], data['slot'],
                               data['start_time_millis']]
                phasedata_temp = data['phases']
                # add
                # for i in list(data.keys()):
                #     if i not in ['attachments', 'phases', 'log_records']

                # add
                # phasedata = [x for x in phasedata_temp if x]
                print(len(phasedata_temp))
                for a in phasedata_temp:
                    key_values = list(a['measurements'].keys())
                    key_list_temp.append(key_values)
                    # clear void list
                    # key_list = [x for x in key_list_temp if x]

                print(len(key_list_temp))
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
                print(' ok  !')


if __name__ == '__main__':
    main()
