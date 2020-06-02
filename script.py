def my_function():
    numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers


total = sum(my_function())
print(total)
