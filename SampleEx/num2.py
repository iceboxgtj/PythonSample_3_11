# 2. 점점 밝아지는 전구
level = int(input("밝기 단계(1~4): "))
symbols = ['░', '▒', '▓', '█']
colors = ['\033[90m', '\033[37m', '\033[97m', '\033[93m']

print("전구 밝기: ", end="")
for i in range(max(0, min(level, 4))):
    print(colors[i] + symbols[i] + "\033[0m", end="")
print()