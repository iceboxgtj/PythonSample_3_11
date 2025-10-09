# 7. 초시계
#import time, sys

#for s in range(11):
#    sys.stdout.write(f"\r{str(s//60).zfill(2)}:{str(s%60).zfill(2)}")
#    sys.stdout.flush()
#    time.sleep(1)
#print()

import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

for s in range(11):
    # 커서를 1행 1열로 이동하고, 줄 끝까지 지우고, 시계 표시
    print(f"\033[1;1H\033[K⏱ {s//60:02d}:{s%60:02d}", end="", flush=True)
    time.sleep(1)

print()  # 마지막 줄바꿈