#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
name_dict=OrderedDict()
n=int(input())
for i in range(n):
    names=input()
    name=''.join(x for x in names if not x.isdigit())
    value="".join(x for x in names if x.isdigit())
    value=int(value)
    if name not in name_dict:
        name_dict[name]=value
    else:
        a=name_dict[name]
        name_dict[name]=value+a
for name in name_dict:
    print(name,end="")
    print(name_dict[name])


