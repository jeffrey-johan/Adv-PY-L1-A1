lst = ['Apple' , 'Guava' , 'Mango' , 'Banana' , 'Kiwi']

print("length of list:" , len(lst))
print("First Element :" , lst[0])
print("Last Element :", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated List :", lst)

lst.sort()
print("Sorted List :", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplacation on List :", lst*2)

lst=lst[:3]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)