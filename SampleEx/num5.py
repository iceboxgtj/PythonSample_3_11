# 5. 진행바 애니메이션
import time, sys

bar_len = 16
for p in range(101):
    filled = p * bar_len // 100
    bar = "█"*filled + "-"*(bar_len - filled)
    color = "\033[92m" if p < 100 else "\033[93m"

    sys.stdout.write(f"\r{color}[{bar}] {p}%\033[0m")
    sys.stdout.flush()
    time.sleep(0.03)
    
print("\n완료!")