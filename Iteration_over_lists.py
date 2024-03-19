my_list = [1, 2, 3, "Python", 3.14]

for item in my_list:
    print(item)
########################
print("########################")
for index, item in enumerate(my_list):
    print(index,item,sep='. ')
########################
print("########################")
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)