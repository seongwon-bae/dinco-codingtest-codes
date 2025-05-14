from collections import deque

c = 11
b = 2
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    # 각 위치에 방문한 시간들을 기록
    # visited[1] -> 1번 위치에 방문한 시간을 기록
    # visited[1] = { 0: True, 2: True} -> 0초에 1번에 위치하기도 했고, 2초에 1번에 위치하기도 했음
    # 위 과정을 반복하여 브라운의 현재 시간(time) 모든 위치를 visited에 넣어둔다.
    visited = [{} for _ in range(200001)]

    while cony_loc<200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time
        for i in range(0, len(queue)):
            now_b, now_time = queue.popleft()
            new_b = now_b - 1
            new_time = now_time + 1
            if new_b >=0 and new_time not in visited[new_b]:
                visited[new_b][new_time] = True
                queue.append((new_b, new_time))

            new_b = now_b + 1
            if new_b < 200001 and new_time not in visited[new_b]:
                visited[new_b][new_time] = True
                queue.append((new_b, new_time))

            new_b = now_b * 2
            if new_b < 200001 and new_time not in visited[new_b]:
                visited[new_b][new_time] = True
                queue.append((new_b, new_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))