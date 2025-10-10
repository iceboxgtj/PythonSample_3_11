# 예제 19: 로켓 카운트다운 (Unicode 간단 버전)
import time, os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

# 1) 카운트다운
clear()
print("🚀 ROCKET LAUNCH\n")
for s in range(10, -1, -1):
    print(f"T-{s:2d}", end="\r", flush=True)
    time.sleep(0.25)
print("\nLIFTOFF!\n")
time.sleep(0.5)

# 2) 발사 애니메이션 (🚀 + 연기/화염 이모지)
H = 18                 # 화면 높이(대충)
X = 18                 # 가로 위치(좌우 여백)
smokes = ["", "·", "•", "⁂", "✦", "✧", "✶", "✨", "💥", "🔥", "💨"]

for t in range(H):
    clear()
    print("🚀 ROCKET LAUNCH\n")

    # 로켓의 높이(아래에서 위로 떠오름)
    top = H - t
    print("\n" * top, end="")

    # 로켓 본체
    print(" " *( X+1) + "🚀")

    # 아래 연기/화염(프레임에 따라 변함)
    s = smokes[t % len(smokes)]
    print(" " * (X+1) + s)
    print(" " * X + s + s + s)
    print(" " * (X+1) + s)

    time.sleep(0.2)

clear()
print("✅ MISSION COMPLETE")