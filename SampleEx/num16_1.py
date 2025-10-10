# 16. 스네이크 진행 커서
import time, sys, os
os.system("cls")

width = 30
for t in range(1, width+1):
    head = ">"
    body = "-"*(t-1)
    line = (body + head).rjust(width)
    sys.stdout.write("\r" + line)
    sys.stdout.flush()
    time.sleep(0.06)
print()