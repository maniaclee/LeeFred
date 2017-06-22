import re
from leeflow import Executer, Result


def loadSshDatas():
    file_object = open('/Users/dushang.lp/.ssh/config')
    lines = file_object.readlines()
    data = []
    for line in lines:
        if line.strip():
            line = line.strip()
            words = re.split(r'\s+', line)
            assert len(words) == 2
            data.append({'host': words[0], 'password': words[1]})
    file_object.close()
    return data

def toResult(data):
    result= []
    for d in data:
        result.append(Result())
def searchHost(s):
    pass


if __name__ == '__main__':
    for a in loadSshDatas():
        print a
