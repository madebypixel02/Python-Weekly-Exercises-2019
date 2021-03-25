def fibonacci(n):
    output = []
    for i in range(n + 1):
        if i == 0:
            output.append(0)
        elif i == 1:
            output.append(1)
        elif i > 1:
            item = output[i - 1] + output[i - 2]
            output.append(item)
    return output

# Example of execution
print(fibonacci(20))
