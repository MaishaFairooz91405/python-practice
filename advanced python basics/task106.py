def deep_copy(list1):
    # return [x[:] for x in list1]
    copied_list=list1[:]
    copied_list[0][2] = 7
    return copied_list
    # copied_list[0][2]=7
    # return copied_list

main_list=[[1,2,3],[4,5,2],[6,7,9]]
# copied_list=deep_copy(main_list)
# copied_list[0][2]=7
print(main_list)
print(deep_copy(main_list))
# copied_list[0][2]=7