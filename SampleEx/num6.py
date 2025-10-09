import time, os

n = int(input("체스판 크기(좌수 권장): "))
n = max(2, n)
frames = [("■", "□"), ("□", "■")]

for f in range(30):
    os.system('cls' if os.name == 'nt' else 'clear')
    a, b = frames[f % 2]
    for y in range(n):
        for x in range(n):
            print(a if (x + y) % 2 == 0 else b, end="")
        print()
    time.sleep(0.3)

 
