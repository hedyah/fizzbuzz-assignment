my_numbers = [3,7,21,15,12,4,5,8,11,16,25,9,20,33,45]

for num in my_numbers:
    if num % 3 == 0 and num % 5 == 0 :
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
