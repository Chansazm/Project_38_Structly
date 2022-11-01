def word(arr):
    output = ""
    stack = [(arr[0])]
    for each_word in arr:
        current = stack.pop()
        output += current
        for neighbor in arr[current]:
            stack.append(neighbor)
    return output
        








array = 'The','cat','is','yellow'
print(word(array))