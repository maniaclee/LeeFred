# encoding: utf-8
import json
import os

import time


class Zebra:
    @staticmethod
    def search(tableNames, url):
        time.sleep(1)
        result = []
        for t in tableNames:
            result.extend(Zebra.fetchResult(Zebra.fetchJson(url % t), t))
        # return [Zebra.fetchResult(Zebra.fetchJson(url % t), t) for t in tableNames]
        return result

    @staticmethod
    def fetchResult(s, tableName):
        # a = json.loads(s, object_hook=lambda dictx: TableMapping(dictx))
        a = json.loads(s)
        for e in a:
            e['table'] = tableName
        return a

    @staticmethod
    def fetchJson(url):
        return os.popen(url).readlines()[0]

    @staticmethod
    def tableNames(tableName, num):
        return [tableName + str(e) for e in range(0, num)]


class TableMapping(dict):
    def __init__(self, ip="", port="0", role="", table=""):
        self.ip = ip
        self.port = port
        self.role = role
        self.table = table

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __repr__(self):
        return str(self.__dict__)


#
# httpClient = httplib.HTTPConnection('rds.dp', 80, timeout=30)
# response = httpClient.request('GET', '/i/database/findDatabaseInstance\?name\=HuiOrder0')
#
# print response.status
# print response.reason
# print response.read()

url_template = '''
curl -b "JSESSIONID=521726F90E94C953B8FE900A1AE7B47B;ticket=AAFSsPYAkNKN6Mb0Q6Li8D8gawrtLGDny0apa8Nu2E3W/w8DI+0bdsNI;" http://rds.dp/i/database/findDatabaseInstance\?name\=%s
'''
# print  json.dumps(Zebra.search(Zebra.tableNames('HuiOrderExtra', 32), url_template)).encode('utf-8')
print  json.dumps(Zebra.search(['mopay'], url_template))
