def solve(arr,low,high):
    if low>high:
        return None
    if low==high:
        return arr[low]
    mid = (low+high)//2
    if mid%2==0:
        if arr[mid]==arr[mid+1]:
            return solve(arr,mid+2,high)
        else:
            return solve(arr,low,mid)
    else:
        if arr[mid]==arr[mid-1]:
            return solve(arr,mid+1,high)
        else:
            return solve(arr,low,mid-1)

arr = [1.,1,2,4,4,5,5,6,6]
ans = solve(arr,0,len(arr)-1)
print(ans)