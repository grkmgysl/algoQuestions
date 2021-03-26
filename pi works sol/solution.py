import math


def isPrime(n):
    if n > 1:
        x = int(math.sqrt(n))
        for i in range(2, x + 1):
            if n % i == 0:
                return False
        return True
    return False


# opens file
f = open("input.txt", "r")
# create matrix of input items
mtx = [x.strip("\n").split(" ") for x in f]
# convert strings to int
for k in range(len(mtx)):
    mtx[k] = list(map(int, mtx[k]))


def solution(mtx):
    a = len(mtx)  # 15
    # makes last row prime numbers zero
    for k in range(a):
        if isPrime(mtx[a - 1][k]):
            mtx[a - 1][k] = 0
    # starting from last second row loop through row by row and
    # checks for 2 items below that row, takes the bigger number,
    # adds the bigger number to the number we are looping,
    # when we finish just return the first number of matrix
    for i in range(a - 2, -1, -1):
        for j in range(0, len(mtx[i])):
            # before checking for bigger we need to check
            # if its prime or not
            if isPrime(mtx[i][j]):
                mtx[i][j] = 0
            else:
                if mtx[i + 1][j] > mtx[i + 1][j + 1]:
                    mtx[i][j] += mtx[i + 1][j]
                elif mtx[i + 1][j + 1] > mtx[i + 1][j]:
                    mtx[i][j] += mtx[i + 1][j + 1]
                else:
                    mtx[i][j] = 0
    return mtx[0][0]


print(solution(mtx))
