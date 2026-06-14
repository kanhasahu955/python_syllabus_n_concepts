# move zeros to the last
li = [0, 1, 0, 3, 12]

result = []


for num in li:
    if num != 0:
        result.append(num)
    
    count_zeros = len(li) - len(result)
result.extend([0] * count_zeros)

print(result)


result_compressd = [num for num in li if num != 0]+[0 for num in li if num == 0]
print(result_compressd)