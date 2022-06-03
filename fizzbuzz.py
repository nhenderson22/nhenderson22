x = 1
while x != 101:
    if x % 5 ==0 and x % 3 == 0:
        print("FizzBuzz")
        x=x+1
    elif x % 3 == 0:
        print("Fizz")
        x=x+1
    elif x % 5 == 0:
        print("Buzz")
        x=x+1
    else:
        print(x)
        x=x+1
