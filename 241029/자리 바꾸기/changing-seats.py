n, k = map(int,input().split())
cur = list(range(n+1)) # 현재 i번재 위치에 val의 사람이 있음
change = [list(map(int,input().split())) for _ in range(k)]
seat = [{i} for i in range(n+1)] # 1번부터 앉을 수 있는 곳

seat_pattern = set()
first_pattern = tuple(frozenset(pos) for pos in seat)
seat_pattern.add(first_pattern)

# 같은 패턴이 나오면 종료
while True:
    this_seat = [set() for _ in range(n+1)]
    for x,y in change:
        cur[x],cur[y] = cur[y],cur[x] # 해당 위치에 있는 사람을 바꿈
        seat[cur[x]].add(x)
        seat[cur[y]].add(y)
        this_seat[cur[x]].add(x)
        this_seat[cur[y]].add(y)

    this_pattern = tuple(frozenset(pos) for pos in this_seat)
    if this_pattern in seat_pattern:
        break
    seat_pattern.add(this_pattern)

for i in range(1,n+1):
    print(len(seat[i]))