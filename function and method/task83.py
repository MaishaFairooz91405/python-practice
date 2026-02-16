def factorial(number):
    value=1
    if number<0:
        return "factorial does not exist for negative number"
    elif number<0 or number<1:
        return 1
    else:
        for i in range(1,number+1):
            value=value*i
        return value

print(factorial(5))