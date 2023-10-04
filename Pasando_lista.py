def contar_identificadores_unicos(n, A):
    count = 0
    for i in range(n):
        unique = True
        for j in range(i):
            if A[i] == A[j]:
                unique = False
                break
        if unique:
            count += 1
    
    return count

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    result = contar_identificadores_unicos(n, A)
    print(result)
