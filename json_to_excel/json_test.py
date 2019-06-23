from __future__ import print_function
import json

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre+[key, '{}']
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:                   
                    yield pre+[key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict
def usefun(value):
    print(dict_generator(Value).next())
    # for i in dict_generator(value):
    #     print('.'.join(i[0:-1]), ':', i[-1])        


if __name__ == "__main__":
    sJOSN =  r'C:\Users\Administrator\Desktop\0623_GRR\0623\a.json'
    fs = open(sJOSN, 'r')
    a = fs.read()
    Value = json.loads(a)
    fs.close()
    usefun(Value)
    # print(dict_generator(Value).next())
    # for i in dict_generator(Value):
    #     print(i)
    #     print('.'.join(i[0:-1]), ':', i[-1])

#output:[u'phases', u'status', u'PASS']