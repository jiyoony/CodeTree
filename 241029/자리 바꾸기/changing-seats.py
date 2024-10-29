n, k = map(int,input().split())
cur = list(range(n+1)) # 현재 i번재 위치에 val의 사람이 있음
change = [list(map(int,input().split())) for _ in range(k)]
seat = [{i} for i in range(n+1)] # 1번부터 앉을 수 있는 곳

first_seat = [{i} for i in range(n+1)]
turn = 0
# 같은 패턴이 나오면 종료
while True:
    turn += 1
    this_seat = [{i} for i in range(n+1)]
    for i in range(k):
    # 자리 바꾸기
        x,y = change[i] # x,y 자리 
        cur[x],cur[y] = cur[y],cur[x] # 해당 위치에 있는 사람을 바꿈
        seat[cur[x]].add(x)
        seat[cur[y]].add(y)
        if turn == 1:
            first_seat[cur[x]].add(x)
            first_seat[cur[y]].add(y)
            first = False
        else:
            this_seat[cur[x]].add(x)
            this_seat[cur[y]].add(y)
    if first_seat == this_seat:
        break

for i in range(1,n+1):
    print(len(seat[i]))