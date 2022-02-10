def twoDArray(size):        #function definition
    array_input = []
    for x in range(size):
        array_input.append([int(y) for y in input().split()])  #2-D array
    print(array_input)

#user inputs
size = int(input("Enter the array size"))
twoDArray(size)         #function call