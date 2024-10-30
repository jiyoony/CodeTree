# n, k = map(int,input().split())
# cur = list(range(n+1)) # 현재 i번재 위치에 val의 사람이 있음
# change = [list(map(int,input().split())) for _ in range(k)]
# seat = [{i} for i in range(n+1)] # 1번부터 앉을 수 있는 곳

# for i in range(3):
#     for x,y in change:
#         seat[cur[x]].add(y)
#         seat[cur[y]].add(x)
#         cur[x],cur[y] = cur[y],cur[x] # 해당 위치에 있는 사람을 바꿈

# for i in range(1,n+1):
#     print(len(seat[i]))
    
    
n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]

can_sit = [{i} for i in range(1, n + 1)]
switch_seat = [
    list(map(int, input().split()))
    for _ in range(k)
]
for i in range(3 * k):
    index = i % k
    can_sit[arr[switch_seat[index][0] - 1] - 1].add(switch_seat[index][1])
    can_sit[arr[switch_seat[index][1] - 1] - 1].add(switch_seat[index][0])
    arr[switch_seat[index][0] - 1], arr[switch_seat[index][1] - 1] = arr[switch_seat[index][1] - 1], arr[switch_seat[index][0] - 1]
for i in range(len(can_sit)):
    print(len(can_sit[i]))