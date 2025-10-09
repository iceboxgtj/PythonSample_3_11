# 3. 타겟 패턴(마름모)
n = int(input("크기 입력: "))

for y in range(-n, n+1):
    for x in range(-n, n+1):
        print("O" if abs(x)+abs(y) <= n else " ", end="")
    print()