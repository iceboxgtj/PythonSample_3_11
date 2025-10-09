# 10. 구구단 컬러 매트릭스
colors = ["\033[31m","\033[32m","\033[33m","\033[34m",
          "\033[35m","\033[36m","\033[91m","\033[92m"]

for i, dan in enumerate(range(2,10)):
    c = colors[i % len(colors)]

    for n in range(1,10):
        print(f"{c}{dan:>2} x {n:>2} = {dan*n:>2}\033[0m", end=" ")
    print()