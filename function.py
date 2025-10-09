#高阶函数
#f = abs
#print(f(-10))#可以把函数赋值给变量
from functools import reduce

def add(x,y,f):
    return f(x) + f(y)
print(add(4,-9,abs))

#map函数，可以把一个函数作用在一个list或者tuple上

r = map(lambda x: x*x,[1,2,3,4])
print(list(r))

#reduce函数，可以把一个函数累积作用在一个序列上,如f(f(f(x1,x2),x3),x4)
print(reduce(lambda x,y:x * y,range(1,10)))#利用reduce计算10!

def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam','LISA','bArT']
L2 = list(map(normalize,L1))
print(L2)

#filter()函数用于过滤序列

#埃氏筛法获取素数序列
def _nature_iter():#构建一个自然数序列
    n = 1
    while True:
        n += 1
        yield n
def _not_divisible(p): #定义筛选函数
    return lambda x: x % p > 0
def primes(): #定义生成器
    it = _nature_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

#for n in primes():
#    if n < 100:
#        print(n)
#    else:
#        break

def is_palindrome(n): #判断一个数是否为回文数
    L = 0
    m = n
    while n > 0:
        L *= 10
        L += n%10
        n = n // 10
    return L == m

