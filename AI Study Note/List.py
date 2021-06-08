# original list
a = [1, 2, 3, 4, "m", 6]
b = ["a", "b", "c", "d", 2, 9, 10]

# append(), add an item to the end of  already existing list
c = 8
a.append(c) # interger append
print(a) # [1, 2, 3, 4, 'm', 6, 8]

d = "Ayuba"
b.append(d)
print(b) # ['a', 'b', 'c', 'd', 2, 9, 10, 'Ayuba']

# extend(), add all items to the to end of already existing list
a.extend(b)
print(a) # [1, 2, 3, 4, 'm', 6, 8, 'a', 'b', 'c', 'd', 2, 9, 10, 'Ayuba']

# insert(), insert an item at the a given position, first argument is the index and second argument is what is what to be inserted
first_names = ["ayuba", "zsuzsanna"]

first_names.insert(1, "tahiru")
first_names.insert(2, "imri")
print(first_names) # ['ayuba', 'tahiru', 'imri', 'zsuzsanna']
