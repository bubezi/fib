def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
   
    
def fib_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(fib(i))
    return numbers


numbers = fib_numbers(10)
print(numbers)
print(len(numbers))
