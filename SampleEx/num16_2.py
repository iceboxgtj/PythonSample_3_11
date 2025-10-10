# 16. 스네이크 진행 커서
import time, sys, os
os.system("cls")

width = 30
for t in range(1, width+1):
    head = ">"
    body = "-"*(t-1)
    line = (body + head).rjust(width)
    print("\033[1;1H",line,flush=True)
    
    time.sleep(0.06)
print()