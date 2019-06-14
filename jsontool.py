#author:Mike
# -*- coding=UTF-8 -*-
import os
import json
import time
import csv
class jsonparser(object):
    # @property
    # def filepath(self):
    #     return self.filepath
    # @property
    # def csvpath(self):
    #     return self.csvpath
    
    # @filepath.setter
    # def filepath(self,filepath):
    #     self.filepath = filepath
    # @csvpath.setter
    # def csvpath(self,csvpath):
    #     self.csvfile = csvfile
    @classmethod
    def jsontocsv(cls):
        global csvfile
        outcome_list = []
        key_list_temp = []
        filenames = []
        #json文件所在地址
        filepath = r'C:\Users\Administrator\Desktop\aa\g502_ralstouch01(NEW)2019-05-23\g501_ralstouch01(NEW)2019-05-23'
        #输出的csv文件位置
        csvpath = r'./'
        #收集目标文件夹里的所有json
        for i in os.listdir(filepath):
            if not i.endswith('.json'):
                continue
            filenames.append(i)
        csvname_time = time.strftime("%m-%d_%H-%M", time.localtime(int(time.time())))
        csvname = 'log' + csvname_time + '.csv' 
        csvfile = os.path.join(csvpath,csvname)
        ##This for py2.7
        # with open('log' + csvname + '.csv', 'wb') as result:
        with open(csvfile, 'w+', newline='') as result:
            result_write = csv.writer(result, delimiter=',')
            count = 0
            for filename, m in zip(filenames, range(len(filenames))):
                print(filename)
                print(count)
                count += 1
                with open(os.path.join(filepath,filename), 'r') as fs:
                    json_data = fs.read()
                    data = json.loads(json_data)
                    cycletime_temp = int(data['end_time_millis']) - int(data['start_time_millis'])
                    cycletime = cycletime_temp/1000
                    # print(time_trans(data['start_time_millis']))
                    other_keys = ['dut_id', 'station_id', 'outcome', 'test_mode', 'slot', 'start_time_millis', 'end_time_millis', 'cycletime']
                    other_items = [data['dut_id'], data['station_id'], data['outcome'], data['test_mode'], data['slot'],
                                   cls.time_trans(data['start_time_millis']), cls.time_trans(data['end_time_millis']), cycletime]
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
                        keyobj = other_keys + first_row
                        result_write.writerow(keyobj)
                    valueobj = other_items + outcome_list
                    result_write.writerow(valueobj)
                    #initial
                    outcome_list = []
                    key_list_temp = []
                    # result.close()
            print('OK!!')
            return csvfile
    @classmethod
    def time_trans(cls,timedata):
        if len(str(int(timedata))) == 10:
            timeStamp = float(timedata)
        else:
            timeStamp = float(timedata) / 1000
        timeArray = time.localtime(timeStamp)
        timestyle = time.strftime("%y-%m-%d,%H:%M:%S", timeArray)
        return timestyle
    #API
    @classmethod
    def getcsv(cls):
        global cf_reader
        cls.jsontocsv()
        cf = open(csvfile,'r')
        cf_reader = csv.reader(cf)
            # print(list(cf_reader))
        return cf_reader


def main():
    # jsonparser().filepath = r'C:\Users\Administrator\Desktop\aa\g502_ralstouch01(NEW)2019-05-23\g501_ralstouch01(NEW)2019-05-23'
    # jsonprser().csvpath = r'./'
    jsonparser.getcsv()
    

if __name__ == '__main__':
    main()
    