if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a=max(arr)
    while a in arr:
        arr.remove(a)
    print(arr[-1])

    
