for x in range(100):

    if x % 3 == 0 and x % 5 == 0:
        print(f"FizzBuzz")
        continue

    elif x % 3 == 0:
        print(f"Fizz")
        continue

    elif x % 5 == 0:
        print(f"Buzz")
        continue

    else:
        print(x)



