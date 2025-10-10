# 13. 주사위 시뮬
import random , os

os.system("cls")

faces = {
    1: ("\033[90m","⚀"),
    2: ("\033[34m","⚁"),
    3: ("\033[32m","⚂"),
    4: ("\033[33m","⚃"),

    5: ("\033[35m","⚄"),
    6: ("\033[31m","⚅")
}

while True:
    s = input("Enter=roll, q=quit: ")
    if s.lower()=="q": break
    n = random.randint(1,6)
    c, sym = faces[n]
    print(f"{c} {sym} \033[0m")  