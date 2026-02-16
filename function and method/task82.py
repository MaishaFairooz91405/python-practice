def prime_number_checker(num):

    if num < 1:
        return "Not prime"

    for i in range(2, num):
        if num % i == 0:
            return "Prime"
            break
    else:
       return "Not prime"

print(prime_number_checker(11))

