#!/usr/bin/python
# coding=gbk
import binascii

from leeflow import Result, Runner

__author__ = 'lipeng'

services = ['mopay-service', 'unicashier-order-service', 'unicashier-service', 'hui-order-service', 'hui-mt-web',
            'hui-business-service']

dbs = [
    Result(title='mopay-online-slave',
           arg='http://rds.dp/;jsessionid=0F98F34F78E8711FDC673197AB8B2B12#/sqleditor/10.1.110.168:3306/MOPay'),
    Result(title='mopay-online-master',
           arg='http://rds.dp/;jsessionid=0F98F34F78E8711FDC673197AB8B2B12#/sqleditor/10.1.110.121:3306/MOPay'),
    Result(title='mopay-beta',
           arg='http://rds.dp/;jsessionid=0F98F34F78E8711FDC673197AB8B2B12#/sqleditor/10.66.7.32:3306/MOPay'),
]


def mopay(input):
    return Runner(results=dbs).run(input)


def crc32(s):
    return binascii.crc32(s) & 0xffffffff


'''
search shard by crc
'''


def huiOrderExtraCrc32(id):
    return shard(crc32(id), 'http://rds.dp/#/database/HuiOrderExtra%s/config')


'''
search shard by id
'''


def huiOrderExtra(id):
    return shard(id, 'http://rds.dp/#/database/HuiOrderExtra%s/config')


def shard(id, url):
    id = long(id)
    if id < 1000:
        db = id
        table = 0
    else:
        db = id % 32
        table = id / 32 % 32
    url = url % db
    return Result(title='db-' + str(db), subtitle="table-" + str(table), arg=url).toFeedBack()

def toHuiOrder(id):
    pass

def toHuiOrder(id):
    pass


# class CodeFlowFinder(FlowFinder):
#     '''
#     想要调用super,父类必须是新类(继承object),不能是经典类(什么都不继承)
#     '''


if __name__ == '__main__':
    print huiOrderExtra(160715111111253)
    print mopay("mopays")
    print mopay("")
    print "true" if "\t\ns".strip() else "false"
    # 3421846044
    print crc32('12345')
