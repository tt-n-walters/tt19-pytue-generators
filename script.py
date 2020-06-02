def my_function(maximum):
    numbers = []
    for i in range(maximum):
        numbers.append(i)
    return numbers


total = sum(my_function(20))
print(total)
