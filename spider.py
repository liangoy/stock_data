import tushare as ts
import pymongo
import time
from functools import reduce
from fn import mr
'''
databases
'''

'''
transaction data
'''


def get_transaction_data_today():
    # input:
    # output:
    # other:
    p = ts.get_today_all()
    today = reduce(lambda x, y: str(x) + (',0' + str(y))[-2:], time.localtime()[:3])
    fn = lambda s: reduce(lambda x, y: str(x) + ',' + str(y),
                          [s['code'], today, s['open'], s['trade'], s['high'], s['low'], s['amount'], s['volume'],
                           s['per'], s['pb'], s['mktcap'], s['nmc']])
    lis = [fn(p.ix[i]) for i in p.index]
    return lis
