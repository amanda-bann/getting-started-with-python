years_list = [5,7,12,13,9,21,11,10]
num_eligible = 0
for year in years_list:
    if year > 9:
        num_eligible = num_eligible +1

print("Number of eligible colleagues:", num_eligible)