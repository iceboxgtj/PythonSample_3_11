# 4. 홀짝 색 구분
for i in range(1, 21):
    c = "\033[34m" if i % 2 else "\033[31m"
    print(f"{c}{i}\033[0m", end=" ")
print()