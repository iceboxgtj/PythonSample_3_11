# 8. 피라미드
h = int(input("높이: "))
mode = int(input("모양(1:정, 2:역): "))

if mode == 1:
    for i in range(1, h+1):
        print(" "*(h-i) + "*"*(2*i-1))

else:
    for i in range(h, 0, -1):
        print(" "*(h-i) + "*"*(2*i-1))