Input = [4, 1, 3, 5, 6, 7, 5, 8]
temp = []
j = 1
count = 1
while j < len(Input):
    if Input[j] >= Input[j - 1]:
        count += 1
    else:
        temp.append(count)
        count = 1
    j += 1
print(temp)

max = temp[0]
sum = 0
for i in temp:
    if i > max:
        max = i
