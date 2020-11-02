#Python 3
#Writing Effective Python
#Slicing Sequences

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[-4:])
print('Middle two:', a[3:-3])

#leaving out the 0 to help reduce visual noise

assert a[5:] == a [0:5]

#when slicing end of a list you should levae out the final index because its redundant
assert a[5:] == a[5:len(a)]

a[:] 
a[:5]
a[:-1]
a[4:]
a[-3:]
a[2:5]
a[2:-1]
a[-3:-1]

#example of slicing the first or last parts of a list
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

#whole new list is made
b = a[4:]
print('Before ', a)
a[2:7] = [99, 22, 14]
print('After  ', a)

#leaving out both the start ande end indexes 
#when slicing ends up with a copy of the orignial list
b = a
assert b == a and b is not a

#assiging a slice with no start or end 
#indexes will replace its entire contents with a copy of whats referenced
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b
print('After', a)

