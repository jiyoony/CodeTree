maps = [list(map(int,input().split())) for _ in range(4)]

dr = input()

if dr == 'R':
    for i in range(4):
        tmp = []
        engage = False
        for j in range(3,-1,-1):
            if maps[i][j] == 0:
                continue
            elif tmp and tmp[-1] != maps[i][j]: # 합체하지 않는 경우
                tmp.append(maps[i][j])
            elif tmp and tmp[-1] == maps[i][j] and not engage:
                tmp[-1] += maps[i][j]
                engage = True
            else:
                tmp.append(maps[i][j])
                engage = False
        
        while len(tmp) < 4:
            tmp.append(0)
        maps[i] = tmp[::-1]

elif dr == 'L':
    for i in range(4):
        tmp = []
        engage = False
        for j in range(4):
            if maps[i][j] == 0:
                continue
            elif tmp and tmp[-1] != maps[i][j]: # 합체하지 않는 경우
                tmp.append(maps[i][j])
            elif tmp and tmp[-1] == maps[i][j] and not engage:
                tmp[-1] += maps[i][j]
                engage = True
            else:
                tmp.append(maps[i][j])
                engage = False
        
        while len(tmp) < 4:
            tmp.append(0)
        maps[i] = tmp

elif dr == 'U':
    for i in range(4): 
        tmp = []
        engage = False
        for j in range(4):
            if maps[j][i] == 0:
                continue
            elif tmp and tmp[-1] != maps[j][i]: # 합체하지 않는 경우
                tmp.append(maps[j][i])
            elif tmp and tmp[-1] == maps[j][i] and not engage:
                tmp[-1] += maps[j][i]
                engage = True
            else:
                tmp.append(maps[j][i])
                engage = False
        while len(tmp) < 4:
            tmp.append(0)
        for j in range(4):
            maps[j][i] = tmp[j]
elif dr == 'D':
    for i in range(4): 
        tmp = []
        engage = False
        for j in range(3,-1,-1):
            if maps[j][i] == 0:
                continue
            elif tmp and tmp[-1] != maps[j][i]: # 합체하지 않는 경우
                tmp.append(maps[j][i])
            elif tmp and tmp[-1] == maps[j][i] and not engage:
                tmp[-1] += maps[j][i]
                engage = True
            else:
                tmp.append(maps[j][i])
                engage = False
        while len(tmp) < 4:
            tmp.append(0)
        for j in range(4):
            maps[j][i] = tmp[-(j+1)]


for i in range(4):
    for j in range(4):
        print(int(maps[i][j]),end = ' ')
    print()