def binrayArray(A):
    z = A.count(0)
    k = 0
    while z:
        A[k]=0
        z = z-1
        k = k+1
    for a in range(k,len(A)):
        A[a] = 1



if __name__=="__main__":
    A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    binrayArray(A)

    print(A)