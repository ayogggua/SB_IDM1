import pysnooper


class IDM1_SB(object):

    def __init__(self, name, gender, department, S_level, SB_level):
        self._name = name
        self._gender = gender
        self.department = department
        self.S_level = S_level
        self.SB_level = SB_level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def information(self):
        print('name:%s,gender:%s,department:%s,S_level:%s,SB_level:%s' \
              % (self.name, self.gender, self.department, self.S_level, self.SB_level))


@pysnooper.snoop()
def main():
    mike = IDM1_SB('Mike', 'F', 'PD', 2, 0)
    print(mike.name)
    mike.name = 'wenzhichao'
    print(mike.name)


if __name__ == '__main__':
    main()
