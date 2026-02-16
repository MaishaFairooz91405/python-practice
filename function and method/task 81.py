def vowel_counter(var_one):
    var_one=var_one.lower()
    var_one=var_one.replace(" ","")
    # print(var_one)
    variable="aeiou"
    count1=0

    for i in variable:
        count1+=var_one.count(i)
    return count1

print(vowel_counter("Maisha Fairooz"))