 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
men=['Li','liu','chen']
men
men.append('zhang')
men.insert(4,'liao')
print(men)
men.pop(4)
print(men)
p=['xia','bin']
men.append(p)
men[5][1]
len(men)
name=input('please input the name that you think is handsome')
content=[name,'is','a','pig']

age=input('please input your age:\n')
age=int(age)
print('Your age is',age)
if age>=18:
    print('adult')
elif age>=12:
    print('teenager')
else:
    print('kid')
    
m=input('please input the weight of a person:\n')
m=int(m)
h=input('please input the height of the corresponding person:\n')
h=float(h)
BMI=m/pow(h,2)
if BMI<=18.5:
    print('weak')
elif BMI<=25:
    print('normal')
elif BMI<=28:
    print('a litte fat')
elif BMI<=32:
    print('fat')
else:
    print('very fat')
    
Digital=input('please input the digital you want to sum:\n')
sum=0
Digital=int(Digital)
for x in range(Digital):
    sum=sum+x
print(sum)

sum=0
i=1
while i<=100:
    sum=sum+i
    i=i+1
print(sum)
  
L=['Bart','Lisa','Adam']
for x in L:
    print('Hello,%s'%x)
    
L=['zhang','liu','liao']
i=0
length=len(L)
while i<length:
    print('Hello,%s'%L[i])
    i=i+1
    
d={'chenyao':100,'liguannan':99,'liuyang':99}
d.get('liguannan')
d.pop('liuyang')

s=set([1,2,3,4])
s.add(5)
print(s)
s.remove(1)
print(s)
ss=set([3,4,5,6])
print(s&ss)
print(s|ss)

n=input('please input an integer:\n')
n=int(n)
print('We transform it into a hexadecimal representation:\n',hex(n))

#求解一元二次方程
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('not a number')
    delta=b*b-4*a*c
    x1=(-1*b+math.sqrt(delta))/(2*a)
    x2=(-1*b-math.sqrt(delta))/(2*a)
    if delta>0:
        print('The Equation has two results\n')
        return x1,x2
    elif delta==0:
        print('The Equation has two equale results\n')
        return x1
    else:
        print('The Equation has no results in the Real range ')
        
#定义x^n
def power(x,n):
    s=1
    for i in range(n):
        if i<=n:
            s=x*s
    return s
        
#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def fact_1(n):
    s=1
    for i in range(n+1):
        if i==0:
            continue
        s=i*s
    return s
        
for i in range(1,10,2):
    print(i)

#用递归解决Tower of Hanoi问题
def move(n,a,b,c):
    if n==1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

L=[]
for i in range(1,100,2):
    L.append(i)
    
for i in 'hello':
    print(i)

#删除字符串首位的空格
def trim(s):
   if len(s)==0:
       return s 
   elif s[0]==' ':
       return trim(s[1:])
   elif s[-1]==' ':
       return trim(s[:-1])
   else:
       return s
    
 #判断一个对象是否可迭代
 from collections import Iterable
 isinstance('abc',Iterable)
 isinstance([1,2,3],Iterable)
 isinstance(123,Iterable)
        
 for i,value in enumerate([(1,1),(2,2),3]):
     print(i,value)
    
#用迭代查找list中的最大值和最小值，并返回一个tuple
def findMinAndMax(L):
    from collections import Iterable
    if isinstance(L,Iterable)==False:
        print('not Iterable')
    elif len(L)==0:
        print('没有输入数据')
    else:
        t_min=L[0]
        t_max=L[0]
        for i in L:
            if i<t_min:
                t_min=i
            if i>t_max:
                t_max=i
        print('最小值和最大值分别是：\n')
        return (t_min,t_max)
        
        
#List comprehensions
[x for x in range(1,11)]
[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0]
[x+y for x in [1,2,3] for y in [4,5]]

L=['Hello','World',18,'Apple']
[s.lower() for s in L if isinstance(s,str)==True]

#打印Fibonacci数列的前N个数
def fibnacci(N):
    n,a,b=1,0,1
    while n<=N:
        print(b)
        a,b,n=b,a+b,n+1

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        n,a,b=n+1,b,a+b
    return 'done'
      
#杨辉三角
def triangles(max):
    L=[[1]]
    if max==0:
        print('请输入正数')
    elif max==1:
        print(L[0])
    else:
        for n in range(max-1):
            a=L[n]
            ll=[1]+[a[m]+a[m+1] for m in range(len(a)-1)]+[1]
            L.append(ll)
        for j in L:
            print(j)
#用generator生成杨辉三角
def triangles(max):
    L=[[1]]
    if max==0:
        print('请输入正数')
    elif max==1:
        yield L[0]
    else:
        for n in range(max-1):
            m=L[n][:len(L[n])-1]
            n=L[n][1:]
            ll=[1]
            for i in range(len(m)):
                ll.append(m[i]+n[i])
            ll.append(1)
            L.append(ll)
        for j in L:
            yield j
n = 0
results = []
for t in triangles(100):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
     
 
def add(x,y,f):
    return f(x)+f(y)
  
list1 = [1,6,2,5,3]
list2 = [34,67,13,678,67]
[list1[i]+list2[i] for i in range(len(list1))]

x=map(abs,[-1,-2,-3])

from functools import reduce
def add(x,y):
    return x+y
reduce(add,range(101))

#规范输入的姓名
def normalize(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

#利用reduce编写一个求积函数
def fn(x,y):
    return x*y

def prod(L):
    from functools import reduce
    return reduce(fn,L)
 
    
    
#将一个字符串转化成浮点数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    
    def str2num(l):
        return DIGITS[l]
    
    for i in range(len(s)):
        if s[i]=='.':
            po=i
    s1,s2=s[:po],s[po+1:]
    ss2=[]
    print(s2)
    for t in range(len(s2)-1,-1,-1):
        ss2.append(s2[t])
    ss2.append('0')
    from functools import reduce
    S1=reduce(lambda x, y: x * 10 + y,map(str2num,s1))
    S2=reduce(lambda x, y: x * 0.1 + y,map(str2num,ss2))
    return S1+S2
    
#删选素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n #用生成器产生奇数序列
        
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<100:
        print(n)
    else:
        break

#用filter删选出回数
def is_palindrome(n):
    n=str(n)
    nn=[]
    for t in n:
        nn.append(t)
    nb=[]
    for i in range(len(n)-1,-1,-1):
        nb.append(n[i])
    return nn==nb

output=filter(is_palindrome,range(1,1000))
print('1~1000:',list(output))
   
#分别按照名字和成绩来排序     
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  
L1=sorted(L,key=lambda t:t[0])
L2=sorted(L,key=lambda t:t[1])
L3=sorted(L,key=lambda t:t[0],reverse=True)
    
#返回函数
def cal_sum(*args):
    ax=0
    for i in args:
        ax=ax+i
    return ax

def lazy_sum(*args):
    def sum():
        ax=0
        for i in args:
            ax=ax+i
        return ax
    return sum

def build(x,y):
    return lambda:x*x+y*y

L=list(filter(lambda x:x%2==1,range(1,20)))

#one test
a=int(input('请输入去年的成绩：'))
b=int(input('请输入今年的成绩：'))
r=(b/a-1)*100
t=b/a-1
print('进步了：%.2f' % r,'%')
print('growth rate:%.2f %%' % t)

for i in range(-1,-1*len(L)-1,-1):
    print(L[i])

sum([x for x in range(1,101) if x%2==1])


def cal(*nums):
    s=1
    for i in nums:
        s=s*i
    return s

def fac(num):
    s=1
    for i in range(1,num+1):
        s=s*i
    return s

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    

def trim(s):
    m,n=0,0
    for i in range(len(s)):
        if s[i]!=' ':
            m=i
            break
    for j in range(len(s)-1,-1,-1):
        if s[j]!=' ':
            n=j
            break
    return s[m:n+1]
        
for x, y in L:
    print(x,y)
        
def triangles(n):
    s=[[1]]
    if n==1:
        yield s
    else:
        for i in range(1,n):
            ss=s[i-1]
            ll=[1]+[ss[j]+ss[j+1] for j in range(len(ss)-1)]+[1]
            s.append(ll)
    for m in s:
        yield m

n=1
for z in triangles(10):
    if n==5:
        print(z)
        break
    else:
        n=n+1
    
#functional programming
import math
def add_sin(f,*x):
    s=0
    for i in x:
        s=s+f(i)
    return s
       
    
sum(range(1,101))      
    
print('chenyao'*5)
print('chenyao '*5)    

def print_max(a,b):
    '''打印两个数中的最大值。
    
    这两个数都应该是整数'''
    if a>=b:
        print('The maximum is :',a)
    else:
        print('The maximun is :',b)
    
print(print_max._doc_)

import spyder-py3\xiaojianren 
