def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return ("FizzBuzz")
    elif n % 3 == 0:
        return ("Fizz")
    elif n % 5 == 0:
        return ("Buzz")
    else:
        return str(n)
    
lenght = int(input("lenght of array:"))

for i in range (1,lenght):
    print(fizzBuzz(i))