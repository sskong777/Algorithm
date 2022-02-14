#선택정렬(Selection Sort)


numbers = [12,21,4,43,13,45,76,93,54,84,23,46,2,57,88,74]

for i in range(0, len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] =  temp

print(numbers)