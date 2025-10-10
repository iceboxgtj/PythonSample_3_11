# 11. 컬러 스트라이프 이동
import time, os

line = " " * 30
pattern = "===="

for t in range(40):
    pos = t 
    s = (" " * ( pos - len(pattern))) + pattern + (" " * ( len(line)-pos))

    s = s[:len(line)]
    color = "\033[9{}m".format(1 + (t%6))
    os.system("cls")
    print(f"\033[1;1H{color}{s}\033[0m", end="", flush=True)
    time.sleep(0.05)
print()