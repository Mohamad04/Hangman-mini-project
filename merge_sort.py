


def merge_Sort(L,start,end):
    
    if start < end:
        mid = (start + end)//2
        merge_Sort(L, start, mid)
        merge_Sort(L, mid+1, end)
        #merge
        L[start:end+1] = Merge( L[start:mid+1], L[mid+1:end+1] )
    

def Merge(Left, Right):
    C=[]
    i=0
    j=0
    while i !=len(Left) and j !=len(Right):
        if Left[i] < Right[j]:
            C.append(Left[i])
            i +=1
        else:
            C.append(Right[j])
            j +=1

    while i!= len(Left):
        C.append(Left[i])
        i +=1
    
    while j!= len(Right):
        C.append(Right[j])
        j +=1

    return C

