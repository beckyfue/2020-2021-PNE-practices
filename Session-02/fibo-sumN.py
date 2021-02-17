def fibosum(n):
    list_numbers=[0,1]
    counter = 0
    sum = 1
    while counter<=(n-2):
        new_number = list_numbers[-1] + list_numbers[-2]
        sum = sum + new_number
        list_numbers.append(new_number)
        counter += 1
    return "The sum of the first" + str(n) +"terms of the Fibonacci series is : " + str(sum)

our_number = 5
print(fibosum(our_number))
our_number = 10
print(fibosum(our_number))