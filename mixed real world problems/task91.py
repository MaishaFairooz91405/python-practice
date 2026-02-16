

marks=[60,98,87,76,92,79,59,86,49]
grades={}

for i in marks:
    if i >= 90:
     grades[i] = "A+"
    elif i >= 80:
        grades[i] = "A"
    elif i >= 70:
        grades[i]="B"
    else:
       grades[i]="C"
print(grades)
