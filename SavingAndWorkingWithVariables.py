a=1 #a is 1
b=a #b is also 1, since a=1
a=2 #a is now changed to 2, but b still remembers the first value of a, since we changed the value of a in line 3 and b was defined on line 2 
print(a)
print(b)
