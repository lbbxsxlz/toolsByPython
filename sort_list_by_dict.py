#!/usr/bin/python

lst = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]
 

lst.sort(key=lambda k: k[1])
print lst
 

lst.sort(key=lambda k: k[0])
print lst
 

lst.sort(key=lambda k: (k[1], k[0]))
print lst
 

[('d', 2), ('c', 2), ('b', 3), ('a', 4)]
[('a', 4), ('b', 3), ('c', 2), ('d', 2)]
[('c', 2), ('d', 2), ('b', 3), ('a', 4)]
 
lst = [{'level': 19, 'star': 36, 'time': 1},
       {'level': 20, 'star': 40, 'time': 2},
       {'level': 20, 'star': 40, 'time': 3},
       {'level': 20, 'star': 40, 'time': 4},
       {'level': 20, 'star': 40, 'time': 5},
       {'level': 18, 'star': 40, 'time': 1}]
 
lst.sort(key=lambda k: (k.get('time', 0)))
 

lst.sort(key=lambda k: (k.get('level', 0), k.get('star', 0)), reverse=True)

for idx, r in enumerate(lst):
    print 'idx[%d]\tlevel: %d\t star: %d\t time: %d\t' % (idx, r['level'], r['star'],r['time'])
  
