import random
import time
def vcode(chart_len = 4):
    global v_code
    v_chart = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    # print v_chart
    v_chart_list = list(v_chart)
    v_len = len(v_chart)
    v_code_list = []
    # print(v_chart_list)
    for i in range(chart_len):
        index = random.randint(0,v_len - 1)
        print(index)
        v_code_list.append(v_chart_list[index])
    v_code = ''.join(v_code_list)
    print(v_code)
    return v_code

def trigger():
    zhongjianghaoma = 'aJ3f'
    count = 0
    while True:
        time.sleep(0.5)
        count += 1
        print ('%s times'%count)
        vcode()
        zhongjianghaoma = 'aJ3f'
        if zhongjianghaoma == v_code:
          print('zhongjiangle')
          break
        else:
          continue
if __name__ == '__main__':
    trigger()
