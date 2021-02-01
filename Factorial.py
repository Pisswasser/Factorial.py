try:
    input = int(input("enter number without expressions: "))
    loopvar = input
    factorial_list = []
    final = 1

    for item in list(range(loopvar +1)):
        factorial_list.append(item)
    del factorial_list[0]
    factorial_list.reverse()

    for item in factorial_list:
        final *= item
    print(f'factorial : {final}')

except ValueError:
    print("invalid input\nmake sure you are typing number without expressions or alphabets")
except MemoryError:
    print("the heck bro? such a large number you entered!\nplease enter a smaller number")


# del somelist[0]
# realfinal = list(range(loop))
# del realfinal[0]
# print(realfinal)
