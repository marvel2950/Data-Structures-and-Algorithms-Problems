def towerOfHanoi(source,dest,hel,n):
    if n==1:
        print("Plate",n,"from",source,"to",dest)
        return
    towerOfHanoi(source,hel,dest,n-1)
    print("Plate",n,"from",source,"to",dest)
    towerOfHanoi(hel,dest,source,n-1)


towerOfHanoi('s','d','h',3)