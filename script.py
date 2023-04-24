def fib_numbers(n):
    """Returns a list of fibonaci numbers"""
    def fib(x):
        if x<=1:
            return x
        else:
            return fib(x-1) + fib(x-2)
    
    numbers = []
    for i in range(n):
        numbers.append(fib(i))
    return numbers


numbers = fib_numbers(10)
print(numbers)
print(len(numbers))
