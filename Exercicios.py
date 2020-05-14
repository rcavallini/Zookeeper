
'''
a = int(input())
b = int(input())
print(a + b)
'''

# Logical operators have a different priority and it affects the order of evaluation.
# Here are the operators in ascending order of their priorities: or, and, not.
# Having this in mind, consider the following expression:
print(False or not False)  # True

# You might be familiar with ^, the bitwise XOR operator in Python.

str_ = "Hello"
str_ = str_ + str(10)
print(str_)

# put your python code here
#N = int(input())
#K = int(input())
#print(K % N)


#Lucky tickets are a kind of mathematical entertainment.
# A ticket is considered lucky if the sum of the first 3 digits coincides with
# the sum of the last 3 digits of the ticket number.

# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
half2 = int(ticket[-3]) + int(ticket[-2]) + int(ticket[-1])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")