m = int(input())
n = int(input())
list1 = []

def solution(m,n):
    for i in range(n - m + 1):
        div = 2
        if m + i == 1:
            continue

        while(True):
            if m + i == 2:
                list1.append(m+i)
                break
            
            if (m + i) % div == 0:
                break
            div += 1
            
            if div >= m + i :
                list1.append(m+i)
                break
    return list1

ans = solution(m,n)

if len(ans) == 0:
    print(-1)
else:    
    print(sum(ans))
    print(min(ans))