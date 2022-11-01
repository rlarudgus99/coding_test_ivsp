N = int(input())

def solution(N):
    div = 2
    while(True):
        if (N % div == 0):
            N = N / div
            print(f"number  : {N}")
            print(f"divisor : {div}")
        else:
            div += 1

        if (N == 1):
            print("반복문 종료")

            break
solution(N)
