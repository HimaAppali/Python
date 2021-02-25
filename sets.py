#set, collection of unique values
s = set()

#add elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
# can't get duplicate values
s.add(3)
print(s)
#removing elements
s.remove(2)
print(s)
print(f"no of elements : {len(s)}")
