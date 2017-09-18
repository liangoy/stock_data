from functools import reduce

class Mr(list):
    def map(self,fn):
        return Mr([fn(i) for i in self])
    def reduce(self,fn):
        return reduce(fn,self)
    def filter(self,fn):
        return Mr(filter(fn,self))

def mr(l):
    return Mr(l)