def eager_function(maximum):
    numbers = []
    for i in range(maximum):
        numbers.append(i)
    return numbers


def lazy_function(maximum):
    for i in range(maximum):
        yield i



total = sum(my_function(200000000))
print(total)
