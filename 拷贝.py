# import copy
#
# a=[[1,2],[3,4]]
# b=copy.deepcopy(a)
# a[0].append(6)
# print(a)
# print(b)
# print(id(a),id(b))


# print('\n'.join(['\t'.join(['{0}*{1}={2}'.format(i,j,i*j) for j in range(1,i+1)]) for i in range(1,10)]))




# def func(a,b=[]):
# #     print(a,b)
# #     b.append(a)
# #     print(b)
# # func(1)
# # func(1)
# # func(1)
# # func(1)


l=['%d%d%d'%(i,j,l) for l in range(1,6) for j in range(1,6) for i in range(1,6)]
print([c for c in filter(lambda x:(x%10)!=(x%100//10) and (x%100//10)!=(x//100) and (x//100)!=(x%10),map(int,l))])

print(123%100//10)


















