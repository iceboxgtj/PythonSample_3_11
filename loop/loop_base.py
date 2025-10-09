for y in range(5):
    for x in range(5):
        if x == y and x !=2:
            print("\\", end="")
        elif x == 2 and y == 2:    
            print("x",end = "")
        elif x + y == 4:
            print("/", end="")
        else:
            print(" ", end="")
    print()