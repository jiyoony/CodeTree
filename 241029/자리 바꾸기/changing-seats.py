n, k = map(int,input().split())
cur = list(range(n+1)) # 현재 i번재 위치에 val의 사람이 있음
change = [list(map(int,input().split())) for _ in range(k)]
seat = [{i} for i in range(n+1)] # 1번부터 앉을 수 있는 곳


for i in range(3*k+1):
# 자리 바꾸기
    idx = i % k
    x,y = change[idx] # x,y 자리 
    cur[x],cur[y] = cur[y],cur[x] # 해당 위치에 있는 사람을 바꿈
    seat[cur[x]].add(x)
    seat[cur[y]].add(y)


for i in range(1,n+1):
    print(len(seat[i]))