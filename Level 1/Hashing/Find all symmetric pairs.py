def symmetricPairs1(arr):
    pairs = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            alpha = arr[i][::-1]
            if alpha==arr[j]:
                pairs.append(arr[i])
    return pairs

arr = [[1,2],[2,3],[4,5],[3,2],[7,9],[2,1]]
pairs = symmetricPairs1(arr)
print(pairs)

def symmetricPairs2(arr):
    pairs = []
    hash = {}
    for a,b in arr:
        if b in hash and hash[b]==a:
            pairs.append([a,b])
        else:
            hash[a]=b
    return pairs

arr = [[1,2],[2,3],[4,5],[3,2],[7,9],[2,1]]
pairs = symmetricPairs2(arr)
print(pairs)

