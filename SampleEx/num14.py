# 14. 불타는 텍스트
import time, os, sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1) 입력
s = input("문장 입력: ").strip()
if not s: s = "NEON SIGN DEMO"

# 2) 타자 효과
clear()
print("=== NEON SIGN ===\n")
typed = ""
for ch in s:
    typed += ch
    print("\r" + typed, end="", flush=True)
    time.sleep(0.08)
print()
time.sleep(0.4)

# 3) 네온 펄스 애니메이션
# 팔레트: 밝은 컬러 계열 (31~36 + 흰색)
palette = ["31", "33", "32", "36", "34", "35", "97"]  # R, Y, G, C, B, M, W
N = len(palette)

# 총 프레임 수와 속도
frames = 60
delay = 0.06

for t in range(frames):
    # 글자마다 색상을 한 칸씩 밀며 네온처럼 흐르게
    out = []
    for i, ch in enumerate(s):
        idx = (t + i) % N
        # 1;로 밝기(볼드) 주고, 간헐적으로 더 밝게 번쩍(반짝) 처리
        bright = "1;" if (t + i) % 7 in (0, 1) else ""  # 작은 스파클
        out.append(f"\033[{bright}{palette[idx]}m{ch}\033[0m")
    clear()
    print("=== NEON SIGN ===\n")
    print("".join(out))
    print("\n(CTRL+C 로 종료)")
    time.sleep(delay)

# 마무리
print("\033[0m")