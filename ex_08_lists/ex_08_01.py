
# Exercise 1: Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. Then write a function 
# called middle that takes a list and returns a new list that contains all but 
# the first and last elements.

def chop(lst):
    del lst[0]
    del lst[-1]
my_list = [1, 2, 5, 6, 8, 9, 10]
chop_list = chop(my_list)
print(my_list)
print(chop_list)

>>>>>>

# def middle(lst):
#     new = lst[1:]
#     del new[-1]
#     return new

# my_list2 = [1, 2, 5, 6, 8, 9, 10, 13, 15]
# middle_list = middle(my_list2)
# print(my_list2)
# print(middle_list)