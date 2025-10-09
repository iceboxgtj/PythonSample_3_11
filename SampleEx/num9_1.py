# 9. 숫자 미로(텍스트)
import os

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

while (px, py) != goal:
    draw()
    k = input("Move(W/A/S/D): ").lower()[:1]
    nx, ny = px, py

    if k == 'w':
        ny -= 1
    elif k == 's':
        ny += 1
    elif k == 'a':
        nx -= 1
    elif k == 'd':
        nx += 1

    if 0 <= nx < N and 0 <= ny < N:
        px, py = nx, ny

draw()
print("탈출 성공!")