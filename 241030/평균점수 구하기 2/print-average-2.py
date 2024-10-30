n = int(input())
score = list(map(float,input().split()))

print(round(sum(score)/n,1))