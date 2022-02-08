def solution(arr):
    countX = dict()
    countY = dict()
    x = 0
    y = 0
    for v in arr:
        countX[v[0]] = countX.get(v[0], 0) + 1
        countY[v[1]] = countY.get(v[1], 0) + 1
    #     get(i,0)는 내가 아직 dict에 없는 경우 0을 할당합니다. 그래서 그것은 0으로 시작하고 카운터를 증가시키기 위해 1을 계속 추가할 것이다.

    for key, value in countX.items():
        if value == 1:
            x = key

    for key, value in countY.items():
        if value == 1:
            y = key

    return [x, y]


arr = [[1, 4], [3, 4], [3, 10]]
print(solution(arr))
