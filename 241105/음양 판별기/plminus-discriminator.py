n = int(input())

for _ in range(n):
    target = int(input())
    if target == 0:
        print("zero")
    elif target < 0:
        print("minus")
    else:
        print("plus")