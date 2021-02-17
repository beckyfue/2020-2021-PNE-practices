list_numbers = [0,1]
counter = 0
while counter<=8:
    new_number=list_numbers[-1]+list_numbers[-2]
    list_numbers.append(new_number)
    counter+=1
print(list_numbers)
