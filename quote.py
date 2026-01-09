#Single- quoted strings
single_quoted = 'Hello, World!'

#String operations with single-quoted strings
length = len(single_quoted) # Length of the string
upper_case = single_quoted.upper() # Convert to uppercase
lower_case = single_quoted.lower() # Convert to lowercase
contains_substring = 'World' in single_quoted #substring is present


#Printing results
print("Single-quoted string :", single_quoted)
print("Length of the string :", length)
print("Uppercase version:", upper_case)
print("Lowercase version:", lower_case)
print("Contains 'World':", contains_substring)


#Double-quoted strings
double_quoted = "NSTI is awesome!"

#String operations with double-quoted strings
length = len(double_quoted) # Length of the string
replaced_string = double_quoted.replace("awesome", "great") # Replace word
words = double_quoted.split()

#Printing results
print("double-quoted string :", double_quoted)
print("Length of the string :", length)
print("String after replacement :", replaced_string)
print("Words in the string :", words)
