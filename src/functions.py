# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        return "Even!"
    else:
        return "Odd"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# Write a function that doubles that value of an integer
def double(n):
    return n*2

my_int = 10
double(my_int)

# if pass by REFERECNE, my_int = 20 (changed the original)
# if pass by VALUE, my_int = 10 (we modified a copy)
print(my_int)

# Write a function that doubles the value of all numbers in a list
def double_list(l):
    return [i*2 for i in l]

my_list = [2, 7, 23, 11, 4, 87]

print(double_list(my_list))
print(my_list)

def capitalize_name(name):
    full_name = name.split(" ")
    name = full_name[0][0:1].upper() + full_name[0][1:] + " " + full_name[1][0:1].upper() + full_name[1][1:]
    # name = name[0:1].upper() + ??? + name[].upper() + name[:]
    print(name)

my_name = "bryce evans"
capitalize_name(my_name)
print(my_name)

