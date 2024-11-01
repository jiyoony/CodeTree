n = int(input())
nums = list(map(int,input().split()))
answer = []
for num in nums:
    if num % 5 == 0 or num % 7 == 0:
        continue
    else:
        answer.append(num)

print(sum(answer))
print(round(sum(answer)/len(answer),1))