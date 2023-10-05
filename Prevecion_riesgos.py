n, x = map(int, input().split())

pesos = list(map(int, input().split()))

pesos.sort()

num_gondolas = 0

left = 0
right = n - 1

while left <= right:
    if pesos[left] + pesos[right] <= x:
        left += 1
        right -= 1
    else:
        right -= 1
    num_gondolas += 1

print(num_gondolas)