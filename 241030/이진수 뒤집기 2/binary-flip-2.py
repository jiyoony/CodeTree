# 백트래킹?

n = int(input())
cur = list(input())
target = list(input())
min_change = float('inf')

def turn(this,idx,change):
    global min_change
    # 종료 조건
    if idx == n:
        if this == target:
            min_change = min(min_change,change)
        return
    if change >= min_change:
        return

    #이번걸 바꾸고 넘어가는 경우
    change_binary(this,idx) # 새로운 배열을 줘야함
    turn(this,idx+1,change+1)
    # 원 상태로 복구
    change_binary(this,idx)
    # 이번걸 건너뛰는 경우
    turn(this,idx+1,change)

def change_binary(this,idx):
    this[idx] = '0' if this[idx] == '1' else '1'
    if idx != 0:
        this[idx-1] = '0' if this[idx-1] == '1' else '1'
    if idx != n-1:
        this[idx+1] = '0' if this[idx+1] == '1' else '1'
    return this


turn(cur,0,0)
print(min_change if min_change != float('inf') else -1)