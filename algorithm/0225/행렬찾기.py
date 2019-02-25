# https://www.swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhKdvi6ECkDFAS6&contestProbId=AV18LoAqItcCFAZN&probBoxId=AWkErcYKgkoDFAQy&type=PROBLEM&problemBoxTitle=Problem+box_10&problemBoxCnt=2

import sys
sys.stdin = open("행렬찾기.txt")

def countRow(i, j, col_cnt):
    global N
    row_cnt = 0

    for row in range(i, N):
        row_cnt += 1
        if row == (N - 1) or not input_list[row+1][j]:
            break

    for row in range(i, i+row_cnt):
        for col in range(j-col_cnt+1, j+1):
            input_list[row][col] = 0
    return row_cnt

T = int(input())

for tc in range(T):
    N = int(input())
    input_list = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    matrix = []

    row_cnt = 0
    col_cnt = 0

    for i in range(N):
        for j in range(N):
            if input_list[i][j] != 0:
                col_cnt += 1
                if j == (N-1) or input_list[i][j+1] == 0:
                    row_cnt = countRow(i, j, col_cnt)
                    matrix.append([row_cnt, col_cnt])
                    cnt += 1
                    row_cnt = 0
                    col_cnt = 0

    min_index = 0
    for i in range(cnt-1):
        min_index = i
        for j in range(i+1, cnt):
            if matrix[j][0] * matrix[j][1] < matrix[min_index][0] * matrix[min_index][1]:
                min_index = j
        matrix[i], matrix[min_index] = matrix[min_index], matrix[i]

    print(f'#{tc+1} {cnt}', end=" ")

    for i in range(cnt):
        for j in range(2):
            print(matrix[i][j], end=" ")
    print()