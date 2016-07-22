import re

from leeflow import Executer, Result
from ShardTables import ShardTables


def zebraHuiOrder(id):
    return commonSearch(id, 'huiOrder')


def zebraHuiOrderExtra(id):
    result = calDbAndTable(id)
    db = result[0]
    table = result[1]
    print result
    return commonSearch(db, 'huiOrderExtra', lambda x: x.setsubtitle("db:%s table: %s" % (db, table)))


def calDbAndTable(id):
    id = long(id)
    if id < 1000:
        db = id
        table = 0
    else:
        db = id % 32
        table = id / 32 % 32
    return [db, table]


def commonSearch(id, table, handleResult=None):
    id = str(id)
    datas = map(
        lambda x: Result(title=x['table'] + " " + x['role'],
                         arg='http://rds.dp/#/sqleditor/%s:%s/%s' % (x['ip'], x['port'], x['table'])),
        ShardTables[table.lower()])
    ex = Executer(datas)
    return ex.run(id,
                  querymatcher=lambda result, query: result.title.find(query) > 0,
                  resultHandler=handleResult)


# print zebraHuiOrderExtra("16072228590739")

# print ('http://rds.dp/#/sqleditor/%s:%s/%s' % (1, 2, 3))

print re.findall(r"\d+", "12a32bc43jf3")[0]


class zebra:
    def matchtable(self, s, query):
        return re.findall(r"\d+", s)[0] == query.strip()

    def createQuery(self, ip="", port="", database="", sql=""):
        return {"ip": ip, "port": port, "database": database,
                "sql": sql}
    def execQuery(self):
        return os.popen()


a = {"ip": "10.1.77.69", "port": "3306", "database": "HuiOrderExtra30",
     "sql": "SELECT * FROM `Hui_Order_Coupon_Detail1` WHERE `id` = \"5\" LIMIT 10000"}
