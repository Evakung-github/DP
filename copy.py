# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:59:32 2019

@author: eva
"""

a = [1,2,3]

b = a
print(id(a),id(b))

c = a.copy()
print(id(a),id(c))
d = a[:]

print(id(a),id(d))

[1,[2]]+[3,4]