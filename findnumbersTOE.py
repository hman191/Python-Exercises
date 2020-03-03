le_numbers = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5!=0:
        le_numbers.append(i)
    else:
        continue
print(le_numbers)
print("\n")
print("total numbers in list:", len(le_numbers))
