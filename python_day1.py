#print("Hello")
#print("First day after a long time")

#var_1 = 7
#var_2 = 2
#var_3 = var_1 / var_2
#print(var_3)
#print(type(var_3),"and",var_3)


# var_4 = "Let us learn"
# var_5 = "Python"
# var_6 = "{gender} is {role}"
# var_7 = var_6.format(gender="He",role="cricketer")
# print(var_7)

# var_7 = var_6.format(gender="She",role="doctor")
#print(var_7)
#print(var_4+var_5)
#print(var_4,"",var_5)

# test_1 = "****"
#
# for rows in test_1:
#
#     print(rows)


#
# test_2 = list()
# for rows in r:
#     for cols in r:
#         test_2.append(cols+1)
#         print(test_2)

#r = range(5)
#print(r)

# for num in r:
#     print("Name_",str(num))

#print()

# for num in r:
#     for num2 in r:
#         print(str(num2), end =" ")
#     print()

r = range(5)
lst1 = ["*"]
print("\nExercise 1 :\n")

for rows in r:
    r2 = range(rows+1)
    for cols in r2:
        print(lst1[cols], end =" ")
    lst1.append("*")
    print()


lst2 = ["1"]
print("\nExercise 2 :\n")

for rows in r:
    r2 = range(rows+1)
    for cols in r2:
        print(lst2[cols], end =" ")
    lst2.append(str(rows+2))
    print()

lst3 = [5]
print("\nExercise 3 :\n")

for rows in r:
    r2 = range(rows+1)
    for cols in r2:
        print(lst3[cols], end =" ")
    lst3.append(lst3[cols]-1)
    print()

lst4 = [5]
print("\nExercise 4 :\n")

for rows in r:
    r2 = range(rows+1)
    for cols in r2:
        print(lst4[cols], end =" ")
    lst4.append(lst4[cols]-rows-1)
    lst4.sort()
    print()
