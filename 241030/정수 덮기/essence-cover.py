n, l = map(int,input().split())
mid = list(map(int,input().split()))
mid.sort()

answer = 0

max_x = 0
for x in mid:
    if max_x < x+0.5:
        max_x = x+0.5+2
        answer += 1

print(answer)