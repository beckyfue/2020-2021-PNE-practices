def fibon(n):
    list_numbers=[0,1]
    counter = 0
    while counter<=(n-2):
        new_number = list_numbers[-1] + list_numbers[-2]
        list_numbers.append(new_number)
        counter += 1
    return "The " + str(n) +"th Fibonacci term is : " + str(list_numbers[-1])

my_number = 5
print(fibon(my_number))
my_number = 10
print(fibon(my_number))
my_number = 15
print(fibon(my_number))
