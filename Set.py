# 1.Creating Sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A :",set_a)
print("Set B :",set_b)

# 2.Adding and Removing Elements in a Set 
set_a.add(6)
set_a.remove(1)
print("Set A after adding 6 and removing 1 :",set_a)
print("Set A :",set_a)
print("Set B :",set_b)

# 3.Union of Sets
union_set = set_a.union(set_b)
print("Union of Set A and Set B :",union_set)

# 4.Intersection of Sets
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B :", intersection_set)

# 5.Difference of Sets
difference_set = set_a.difference(set_b)
print("Difference of Set A and Set B (A - B) :", difference_set)

# 6.Symmetric Difference of Sets
sym_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of Set A and Set B :",sym_diff_set)

# 7.Subset and Superset Testing
set_c = {4, 5}
is_subset = set_c.issubset(set_a)
is_superset = set_a.issuperset(set_c)
print(f"Is Set C a subset of Set A? {is_subset}")
print(f"Is Set A a superset of Set C? {is_superset}")

# 8.Set Membership Testing
is_member = 3 in set_a
print("Is 3 in Set A?",is_member)

# 9.Removing Duplicates Using Sets
number_list = [1,2,3,4,5,6,6,7,7]
union_numbers = set(number_list)   # Removing duplicates
print("List of numbers after removing duplicates :",union_numbers)

# 10.Set Comprehension
squares_set = {x**2 for x in range(1,11)}
print("Set of squares of numbers form 1 to 10 :",squares_set)

# 11.Clearing a Set
set_a.clear()
print("Set A after cleaning :",set_a)