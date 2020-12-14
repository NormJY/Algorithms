# "Fizz Buzz" is a word game we will use to teach the robots about division.
# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5.
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.

# Input: A number as an integer
# Output: The answer as a string

def fizz_buzz(number: int):
    answer = 'Fizz Buzz'

    if (number % 5 == 0 and number % 3 == 0):
        answer = 'Fizz Buzz'
    elif (number % 3 == 0):
        answer = 'Fizz'
    elif (number % 5 == 0):
        answer = 'Buzz'
    else:
        answer = str(number)
    
    return answer
