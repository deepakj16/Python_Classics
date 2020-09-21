#1. Selection sort -- Finding the lowest and swap.
def Selection_Sorting(Inp_Array):
    print(Inp_Array)
    Sorted=[]
    for i in Inp_Array:
        lowest=max(Inp_Array)
        for j in Inp_Array:
            if j<lowest and (len(Sorted)==0 or j not in Sorted):
                lowest=j
        Sorted.append(lowest)
        print(Sorted)

    return Sorted

def Selection_sort_Swap(Inp_Array):
    for index1,i, in enumerate(Inp_Array):
        lowest = i
        for index2,j in enumerate(Inp_Array):
            if i != j and index2>index1 and j < lowest:
                lowest = j
        tmp_index=Inp_Array.index(lowest)
        tmp_value=Inp_Array[index1]
        Inp_Array[index1]=Inp_Array[tmp_index]
        Inp_Array[tmp_index]= tmp_value
    return Inp_Array

def Check_Sort(Inp_Array):
    for i in range(1,len(Inp_Array)):
        if Inp_Array[i] < Inp_Array[i-1]:
            return 0
    return 1

def Bubble_Sorting(Inp_Array):
    #print(len(Inp_Array))
    for i in range(1, len(Inp_Array)):
        #print(i,Inp_Array[i-1],Inp_Array[i])
        if Inp_Array[i-1] > Inp_Array[i]:
            tmp_value=Inp_Array[i]
            Inp_Array[i]=Inp_Array[i-1]
            Inp_Array[i - 1]=tmp_value

    print(Check_Sort(Inp_Array))

    if Check_Sort(Inp_Array) == 0:
        print(Inp_Array)
        Bubble_Sorting(Inp_Array)
        print(Inp_Array)


def Insertion_Sort(Inp_Array):
    for i in range(1, len(Inp_Array)):
        if Inp_Array[i-1] > Inp_Array[i]:
            tmp_value=Inp_Array[i]
            Inp_Array.pop(i)
            Inp_Array.insert(i-1,tmp_value)
            print(Inp_Array)
            Insertion_Sort(Inp_Array)

    return Inp_Array

def Merge(left_l, right_l):
    Sorted=[]
    leng=len(left_l) + len(right_l)
    print(leng)
    for i in range(leng) :
        if left_l and right_l :
            if left_l[0] > right_l[0]:
                print(left_l[0])
                Sorted.append(right_l[0])
                right_l.pop(0)
            else:
                print(right_l[0])
                Sorted.append(left_l[0])
                left_l.pop(0)
    Sorted+=left_l
    Sorted+=right_l
    return Sorted

def Merge_w(left_l, right_l):
    Sorted = []
    while left_l and right_l:
        if left_l[0] > right_l[0]:
            Sorted.append(right_l.pop(0))
        else:
            Sorted.append(left_l.pop(0))
    Sorted += left_l
    Sorted += right_l
    return Sorted


#print(Merge([4, 6],[5, 7]))
print(Merge_w([4, 6],[5, 7]))

def Merge_Sort(Inp_Array):
    if len(Inp_Array)< 2:
        return Inp_Array

    print(Inp_Array)
    print(len(Inp_Array)//2)
    mid = len(Inp_Array)//2
    Sorted1= Merge_Sort(Inp_Array[:mid])
    Sorted2= Merge_Sort(Inp_Array[mid:])
    Sorted=Sorted1+Sorted2

    #print(Sorted)
    return(Sorted)


Inp_Array = [5,4,6,7,3,2,1]
#print(Selection_Sorting(Inp_Array))
#print(Bubble_Sorting(Inp_Array))
#print(Insertion_Sort(Inp_Array))
#print(Merge_Sort(Inp_Array))








