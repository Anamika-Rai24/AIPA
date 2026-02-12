# 1.Factorial
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# num =int(input("Enter Number :"))
# print("Factorial of",num,"is :",factorial(num))

# 2.Remove duplicate elements from a list without using set() 
# number_list = [1, 2, 3, 4, 5, 6, 6, 7, 7]
# unique_list = []     # new list to store unique values
# for num in number_list:
#     if num not in unique_list:   
#         unique_list.append(num)
# print("List after removing duplicates:", unique_list)

# 3.the second largest value without sorting the list
# list1 = [10,5,20,8,20]
# largest = max(list1)
# new_list = []
# for num in list1:
#     if num != largest:
#         new_list.append(num)
# second_largest = max(new_list)
# print("Second largest number is :",second_largest)

# # 4.Alternate Merge of Two list
# A = [1,3,5]
# B = [2,4,6]
# result = []
# i = 0
# while i<len(A) or i< len(B):
#     if i < len(A):
#         result.append(A[i])
#     if i < len(B):
#         result.append(B[i])
#     i += 1
# print("Merge List :", result)

# 5.Elements that appear in both lists, but without duplicates
# num1 = [1,2,2,3,4,4]
# num2 = [2,3,5,]
# common = []
# for x in num1:
#     if x in num2 and x not in common:
#         common.append(x)
# print(common)

# # 6.Replace element by their square
# squ = [1,2,3,4,5]
# result = [x*x for x in squ]
# print(result)

# # 7.Separate even and odd numbers
# num = [1,2,3,4,5,6,7,8,9]
# even = []
# odd = []
# for n in num:
#     if n % 2 == 0:
#         even.append(n)
#     else:
#         odd.append(n)
# print("Even :",even)
# print("Odd :",odd)

# 8.Rotate list to the right by N steps
# num_list = [1,2,3,4,5,6]
# N = 2
# N = N % len(num_list)
# result = num_list[-N:] + num_list[:-N]
# print(result)

# 9.Elements common in all three lists
A = [1,2,3,4]
B = [2,3,5]
C = [3,2,6]
common = []
for x in A:
    if x in B and x in C and x not in common:
        common.append(x)
print(common)        
