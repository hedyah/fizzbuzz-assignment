my_numbers = [3,7,4,5,8,9,11,15,12,16,21,25,20,33,45]

for num in my_numbers:
    if num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
