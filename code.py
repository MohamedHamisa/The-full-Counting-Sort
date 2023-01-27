def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    arr.sort(key=lambda x: int(x[0]))
    print(*[item[1] for item in arr])
