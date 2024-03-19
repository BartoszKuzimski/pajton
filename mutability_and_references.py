my_string = "Hello, Python!"
try:
    my_string[7] = 'W'
except TypeError as e:
    print(e)

print("#####################################################################")

my_list = [1,2,3,4]
my_list[2] = 30
print(my_list)

print("########################################")

original_list = [1,2,3]
new_list = original_list
new_list[1] = 200
print(original_list)

print("#####################################################################")

independent_copy = original_list[:]
independent_copy[1] = 20
print(original_list)
print(independent_copy)

print("###################################")

a = 10
b = a
b = 5
print(a)
print(b)

print("#####################################################################")

lst1 = [1,2,3]
lst2 = lst1
lst2.append(4)
print(lst1)

print("aaaaaaaaaaaaaaaaaa")

Lst = [50, 70, 30, 20, 90, 10, 50000]
 
# Display list
print(Lst[-7::1])