#
# def p(n):
#     jiu_c=0
#     p_c=0
#     pg_c=0
#     while 1:
#         if n>2:
#             jiu_c += 1
#             p_c += 1
#             pg_c += 1
#             n-=2
#         elif p_c>=4:
#             p_c-=4
#             jiu_c += 1
#             p_c += 1
#             pg_c += 1
#         elif pg_c>=2:
#             pg_c-=2
#             jiu_c += 1
#             p_c += 1
#             pg_c += 1
#         else:
#             break
#
#     print(jiu_c)
#     print(pg_c)
#     print(p_c)
#
#
# p(10)
#
#
#
#
#
#
#
#
#
#
#
# a=[1,2,3]
# b=[4,5,6]
# print(dict(zip(a,b)))
# from functools import reduce
# d=[x for x in map(lambda a:{a[0]:a[1]},zip(a,b))]
# while len(d)>1:
#     d[0].update(d[1])
#     del d[1]
# print(d[0])


# #　is与==的区别
#
# def jiance(a,b):
#     print('值：',a,b)
#     print('类别：',type(a),type(b))
#     print('地址：',id(a),id(b))
#
# a=[1,2,3]
# b=[1,2,3]
# c=a
# print('a==b',a==b)  # True
# print('aisb',a is b)  # False
# jiance(a,b)
#
# print('a==b',a==b)  # True
# print('aisb',a is b)  # True
# jiance(a,b)


# abs()
# dict()
# list()
# tuple()
# int()
# str()
# input()
# print()
# chr()
# type()
# id()
# min()
# max()
# dir()
# format()


# import re
# a='abcdef'
# print(re.match('de',a))
# print(re.search('de',a))
# print(a[3:5])

# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]
#
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]
#
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]
#
# import cProfile,random
# lIn = [random.random() for i in range(100000)]
# cProfile.run('f1(lIn)')
# cProfile.run('f2(lIn)')
# cProfile.run('f3(lIn)')
def a():pass
a()


