# 9. 숫자 미로(텍스트)
import os
import time
import keyboard

N = 5
px, py = 0, 0
goal = (N-1, N-1)

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(N):
        for x in range(N):
            if (x, y) == (px, py):
                print("\033[32mP\033[0m", end=" ")
            elif (x, y) == goal:
                print("\033[33mG\033[0m", end=" ")
            else:
                print(".", end=" ")
        print()

# --- 폴링 루프 ---
pressed = {'w': False, 'a': False, 's': False, 'd': False}
draw()  # 초기 화면

while (px, py) != goal:
    moved = False

    # 키 상태를 계속 확인(폴링)
    for key, dx, dy in (('w', 0, -1), ('s', 0, 1), ('a', -1, 0), ('d', 1, 0)):
        if keyboard.is_pressed(key):
            # 이전 루프에서 눌려있지 않았던 경우에만 1회 이동 (엣지 감지)
            if not pressed[key]:
                nx, ny = px + dx, py + dy
                if 0 <= nx < N and 0 <= ny < N:
                    px, py = nx, ny
                    moved = True
            pressed[key] = True
        else:
            pressed[key] = False

    if moved:
        draw()

    time.sleep(0.02)  # CPU 점유율 낮추기(50fps 정도)

draw()
print("탈출 성공!")