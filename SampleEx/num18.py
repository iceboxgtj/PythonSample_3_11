# 18. ASCII 웨이브
import time, math, os

W = 50
for t in range(40):
    os.system('cls' if os.name=='nt' else 'clear')
    for r in range(8):
        x = int((math.sin(t*0.2 + r*0.5)+1)/2 * (W-1))
        print(" " * x + "*")
    time.sleep(0.07)