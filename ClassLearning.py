# 1. Class/Instance/Attribute/self/property
# 2. Hook/Magic method => Operator Override/__init__/__str__/__call__
# 3. Inherit/多根/单根

class A(object):
     aField = ['TestAField']
     def aMethod(self):
         print(self.aField)
         print('TestAMethod')
     birthday = 1983
     @property
     def age(self):
         return 2018 - self.birthday
# 
# aInstance = A()
# bInstance = A()
# aInstance.aField.append('test')
# aInstance.aField = 'test'
# 
# print(id(A), id(aInstance), id(aInstance.__class__))
# print(A.aField)
# print(aInstance.aField)
# print(bInstance.aField)
# 
# aInstance.aMethod()
# aInstance.__class__.aMethod(aInstance)
# A.aMethod(aInstance)
# 
# aInstance.aField = 'NewField'
# aInstance.aMethod() # A.aMethod(aInstance)
# bInstance.aMethod() # A.aMethod(bInstance)
# 
# print(aInstance.age)
# 
# print(3 + 5)
# print((3).__class__.__add__(3, 5))
# 
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return '<Person::%s>' % self.name
#     def greeting(self):
#         print('[%s]:: Hi~' % self.name)
#
# zhangsan = Person()
# zhangsan.name = 'Zhang San'
# lisi = Person()
# lisi.name = 'Li Si'
# zhangsan = Person('Zhang San', 42)
# lisi = Person('Li Si', 23)
# print(str(zhangsan), lisi)
# zhangsan.greeting()
# lisi.greeting()
# 
# def addN(n):
#     def add(x):
#         return x+n
#     return add
#
# class addN(object):
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, x):
#         return x+self.n
# 
# add3 = addN(3)
# add4 = addN(4)
# print(add3(42)) 
# print(add4(42))
# 
# class Name(str):
#     def getLastName(self):
#         return self.split()[-1]
# 
# zhangsan = Name('Zhang San')
# print(len(zhangsan))
# print(zhangsan.getLastName())
# print(zhangsan.split())