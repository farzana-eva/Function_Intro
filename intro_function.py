def adding(x, y, z):
    result = x + y + z
    return result


answer = adding(4, 6, 9)
print(answer)

for val in range(1, 5):
    adding_value = adding(2, val, 5)
    print(adding_value)


def multiply(x, y):
    result = x * y
    return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)