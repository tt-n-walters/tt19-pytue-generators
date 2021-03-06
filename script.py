def eager_function(maximum):
    numbers = []
    for i in range(maximum):
        numbers.append(i)
    return numbers  # stops the function and sets the output


# Generator
def lazy_function(maximum):
    for i in range(maximum):
        yield i    # pauses the function and sets the output


print(eager_function(10))
generator = lazy_function(10)

for x in generator:
    print(x)





# total = sum(lazy_function(200000000))
# print(total)
