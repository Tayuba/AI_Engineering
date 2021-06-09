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

# remove(x), removes the first item from the list whose values is equal to the "x". raise ValueError if no such item
first_names.remove("ayuba")
print(first_names) # ['tahiru', 'imri', 'zsuzsanna']

# pop([i]), removes the item at the given position in the list, if no position is given, it removes and return the last item
index_zero_pop = first_names.pop(0)
print(index_zero_pop) # tahiru
no_index_pop = first_names.pop()
print(no_index_pop) # zsuzsanna

# clear(), remove all item from the list. equivalent to del a[:]
a.clear()
print(a) # []

del b[:]
print(b) # []


# index(x[,start[,end]]), return zero_base index in the list of the first item whose value is equal to x, Raise a ValueError if there is no such item
b = ["w", "a", "b", "c", "d","d", 2, 9, 10, 10]
indexed_value = b.index(2)
print(indexed_value) # 6

# count(x), returns the number of times x appears in a list
count_value = b.count("d")
print(count_value) # 2

c = ["w", "a", "b", "c", "d","d", "z", "q", "l"]
c.sort()
print(c) # ['a', 'b', 'c', 'd', 'd', 'l', 'q', 'w', 'z']

# reverse(), reverse the element of the list
c.reverse()
print(c) # ['z', 'w', 'q', 'l', 'd', 'd', 'c', 'b', 'a']