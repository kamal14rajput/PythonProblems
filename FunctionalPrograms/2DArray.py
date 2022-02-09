#user inputs
size = int(input("Enter the array size"))
array_input = []
for x in range(size):
    array_input.append([int(y) for y in input().split()])
print(array_input)