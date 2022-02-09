#function for sum of integers equal to zero
def findTriplets(arr,n):
    found = False
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(arr[i] + arr[j] + arr[k] == 0):
                    print("Triplets are:",arr[i], arr[j], arr[k])

                    found = True
    if(found == False):
        print("Triplets not found")

# creating an empty list
arr = []
# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    arr.append(ele)  # adding the element

print(arr)
n = len(arr)
findTriplets(arr,n)   #function call