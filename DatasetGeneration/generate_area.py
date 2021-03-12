# -*- coding: utf-8 -*-
# This program has the purpose of generating a random vector with 'n_areas' 
# combinations of 24 area values from a seed 'a' 
# between 'min' mm ^ 2 and 'max' mm ^ 2

import csv
import random

max = 45.0
min = 75.0
n_areas = 2000
random.seed(a=2)


with open('areas24.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['area_id', *['area{0}'.format(x) for x in range(1,25)]])
    for i in range(n_areas):
        nums = [i]
        for j in range(24):
            num = random.random() * (max - min) + min
            nums.append(num)
        writer.writerow((str(x) for x in nums))
