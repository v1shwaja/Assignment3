def factorial(n):   #function
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


a = int(input('Enter the number: '))
print('Factorial of', a, 'is', factorial(a)) #call