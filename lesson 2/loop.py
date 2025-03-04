# The loop will break if the i is greater than 6
i =  1
while i < 6:
    # print(i)
    i+=1

# The Loop will break if i is equal to 3

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    # print(i)


# For Loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


for x in "banana":
  print(x) 

# Alogrithms 

def find_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

numbers = [10, 5, 8, 20, 3]
print("Maximum number:", find_max(numbers))