# 이분탐색
n = int(input())
nsize = list(map(int,input().split()))
k = int(input()) # 물건 개수
ksize = list(map(int,input().split()))

def min_time_to_remove_items(n,nsize,k,ksize):
    nsize.sort(reverse = True)
    ksize.sort(reverse = True)

    if ksize[0] > nsize[0]:
        return -1
    
    left,right = 1,k
    answer = right # 시간을 기준으로 이분탐색

    while left <= right:
        mid = (left + right) // 2

        # mid 시간내에 모든 물건을 제거 할 수 있는 지 체크
        index = 0
        for c in nsize:
            for _ in range(mid):
                if index < k and ksize[index] <= c:
                    index += 1
                else:
                    break
        
        if index == k: # mid 시간내에 처리 가능
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(min_time_to_remove_items(n,nsize,k,ksize))