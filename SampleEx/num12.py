# 12. 미니 막대 그래프
nums = list(map(int, input("정수 5개:? ? ? ? ?").split()))[:5]
m = max(1, max(nums))

for v in nums:
    bar = "█" * (v * 20 // m)
    print(f"{v:>2} | {bar}")