#https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools as it
data=list(map(int,list(input())))
for key ,grp in it.groupby(data):
    print(('({}, {})'.format(len(list(grp)),key)),end=" ")
print("")
