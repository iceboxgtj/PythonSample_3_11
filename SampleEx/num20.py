# 20. 콘솔 불꽃놀이
import time, os, random

W, H = 40, 12
colors = ["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m","\033[91m"]

for _ in range(25):
    os.system('cls' if os.name=='nt' else 'clear')
    buf = [[" "]*W for _ in range(H)]
    
    for _ in range(random.randint(5,10)):
        x = random.randint(0, W-1)
        y = random.randint(0, H-1)
        c = random.choice(colors)
        buf[y][x] = c + "*" + "\033[0m"
    
    for row in buf:
        print("".join(row))
    time.sleep(0.08)