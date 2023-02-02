def fizz_buzz(num_1):
    return num_1

def divide_3(num_1):
    if num_1 % 3 == 0:
        return "fizz"
    else:
        return f"{num_1} is not divisibile by 3"

def divide_5(num_1):
    if num_1 % 5 == 0:
        return "buzz"
    else:
        return f"{num_1} is not divisible by 5"

def divide_by_3_and_5(num_1):
    if (num_1 % 3 == 0) and (num_1 % 5 == 0): 
        return "fizzbuzz"
    else:
        return str(num_1)


# function 'fizzbuzz' takes in one parameter 
# check parameter divides by 3 - if so, return "fizz" 
    # if num_1 % 3 == 0:
    # return "fizz"
# check parameter divides by 5 - if so, return "buzz" 
    # if num_1 % 5 == 0:
    # return "buzz"
# if parameter divides by 3 & 5 - return "fizzbuzz" 
    # if (num_1 % 3 == 0) and (num_1 % 5 == 0)
    # return "fizzbuzz"

#if parameter not divisibile by 3 or 5 - return parameter as string - convert int to string 



def fizz_buzz_game(num_1):
    if (num_1 % 3 == 0) and (num_1 % 5 == 0):
        return "fizzbuzz"
    elif num_1 % 3 == 0:
        return "fizz"
    elif num_1 % 5 == 0:
        return "buzz"
    else:
        return str(num_1)