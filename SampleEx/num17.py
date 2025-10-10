# 17. 숫자 맞추기
import random

ans = random.randint(1,100)
cnt = 0

while True:
    try:
        x = int(input("숫자(1~100): "))
    except:
        continue

    cnt += 1
    if x < ans:
        print("답은 더 크다!")
    elif x > ans:
        print("답은 더 작다!")
    else:
        print(f"정답! {cnt}번 시도")
        break