n = int(input())

def max_peliculas(n, horarios):
    horarios.sort(key=lambda x: x[1])
    count = 1
    fin = horarios[0][1]

    for i in range(1, n):
        if horarios[i][0] >= fin:
            count += 1
            fin = horarios[i][1]

    return count

horarios = []
for _ in range(n):
    a, b = map(int, input().split())
    horarios.append((a, b))

resultado = max_peliculas(n, horarios)
print(resultado)