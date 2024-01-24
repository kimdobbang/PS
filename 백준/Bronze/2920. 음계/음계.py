note = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = ascending[::-1]

if note == ascending:
    print("ascending")
elif note == descending:
    print("descending")
else:
    print("mixed")