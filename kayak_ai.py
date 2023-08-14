n = int(input())
weights = list(map(int, input().split()))
weights.sort()
min_diff = 0
for i in range(n-1):
    min_diff += abs(weights[i] - weights[2*n-i-2])
print(min_diff)
