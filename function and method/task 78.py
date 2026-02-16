#Built in sum
def addition(*args):
    result=0
    result+=sum(args)
    return result

print(addition(32,21,56,34))
#Manually
def addition(*args):
    result=0
    for i in args:
        result+=i
    return result

print(addition(32,21,56,34))