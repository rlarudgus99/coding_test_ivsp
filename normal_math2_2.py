N = int(input())
list1 = [int(x) for x in input().split()]

def solution(N,list1):
    res = 0
    for i in range(N):
        div = 2

        if list1[i] == 1:
            continue

        while(True):
            if list1[i] == 2:
                res += 1
                break

            if list1[i] % div == 0:
                break
            div += 1
            
            if div >= list1[i] :
                res += 1
                break
            
    return res

print(solution(N,list1))
