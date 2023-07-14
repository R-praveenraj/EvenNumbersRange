#You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
#Each query consists of two integers B[i][0] and B[i][1].
#For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].
#Input  A = [1, 2, 3, 4, 5]  B = [   [0, 2] [2, 4] [1, 4]   ]
# Output [1,1,2]

def Evennumber(array,query):
    lists=[]
    for q in query:
        start=q[0]
        end=q[1]
        count=0
        for i in range(start,end+1):
            if array[i]%2==0:
                count+=1
        lists.append(count)

    return lists



array = [1, 2, 3, 4, 5]
query=[[0, 2],[2, 4],[1, 4]]
print(Evennumber(array,query))