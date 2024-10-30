n = int(input())
cur = list(input())
target = list(input())
min_change = float('inf')

def flip(bits, idx):
    """주어진 인덱스와 인접한 인덱스의 비트를 반전시키는 함수"""
    bits[idx] = '0' if bits[idx] == '1' else '1'
    if idx > 0:
        bits[idx - 1] = '0' if bits[idx - 1] == '1' else '1'
    if idx < n - 1:
        bits[idx + 1] = '0' if bits[idx + 1] == '1' else '1'

def min_switches(cur, target):
    """스위치를 최소로 눌러 목표 배열을 만드는 함수"""
    global min_change
    
    for first_flip in (0, 1):  # 첫 번째 스위치를 누르는 경우와 누르지 않는 경우
        changes = 0
        bits = cur[:]  # 복사본으로 작업
        
        if first_flip == 1:
            flip(bits, 0)
            changes += 1
        
        for i in range(1, n):
            if bits[i - 1] != target[i - 1]:  # 이전 비트가 목표와 다르면 스위치를 누름
                flip(bits, i)
                changes += 1
        
        if bits == target:
            min_change = min(min_change, changes)
    
min_switches(cur, target)
print(min_change if min_change != float('inf') else -1)