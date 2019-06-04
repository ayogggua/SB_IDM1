import random
def vcode(chart_len = 4):
    v_chart = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    print v_chart
    v_chart_list = list(v_chart)
    v_len = len(v_chart)
    v_code_list = []
    print(v_chart_list)
    for i in range(chart_len):
        index = random.randint(0,v_len - 1)
        print(index)
        v_code_list.append(v_chart_list[index])
    v_code = ''.join(v_code_list)
    print(v_code)

vcode()
