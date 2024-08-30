b = {3,4,5,(7,8,9)}
'''
b.add(4)
b.add(5)
b.add(5)
#    not possible to add list
b.add((7,8,9))   #can add tuple, but not dictionary
print(b)
#cannot change items in sets
print(len(b))

b.remove((2))    #removes
print(b)
'''
print(b.pop())
print(b)

b.clear()
print(b)