s  = int(input())

arr = [[None for _ in range(s)]  for _ in range(s)]
   # print ([_ for j in range(s)])

for i in range(s):
    for j in range(s):
        if i <= j and i <= s-1-j:
            arr[i][j] = i + 1
        if i >= j and i >= s-1-j:
            arr[i][j] = s - i
        if i > j and i < s-1-j:
            arr[i][j] = j + 1
        if i < j and i > s-1-j:
            arr[i][j] = s - j
for a in arr:
    print(*a, sep=' ')