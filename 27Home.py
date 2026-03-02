# List:
lst = []

t = (1,2,3,4)
l= (5,6,7,8)
s2 = (3,4,5,6)

# append:
lst.append(10)
lst.append(20.5)
lst.append("Sai")
lst.append(10)
lst.append(False)
lst.append(10)
lst.append(s2)

# insert
lst.insert(1, "python")
print("After insert at index 1:" , lst)

# remove:
lst.remove(10)
print("After remove first 10:", lst)

# pop:
lst.pop()
print("After pop last element:", lst)

# count:
c = lst.count(10)
print("count of 10:",c)
print("Final List:",lst)