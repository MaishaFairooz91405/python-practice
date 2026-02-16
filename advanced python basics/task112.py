# count=0
# def make_counter():
# count = 0

def test_counter():
    count = 0
    def counter():
        nonlocal  count
        count += 1
        return count
    return counter
    # return counter


my_counter = test_counter()
print(my_counter())
print(my_counter())
print(my_counter())