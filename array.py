arr=[1,2,3,52,423,432312,32145]
for num in arr:
    print(num)
print (arr[:-2])
#Find Maximum

maximum=arr[0]
for numbers in arr:
    if numbers>maximum:
        maximum=numbers
print(maximum)