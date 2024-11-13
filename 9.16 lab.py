nums= map(int, input().split())

negatives= sorted([num for num in nums if num < 0], reverse=True)


for num in negatives:
    print(num, end=" ")