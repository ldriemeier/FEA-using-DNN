# -*- coding: utf-8 -*-
# Este programa tem a finalidade de gerar um vetor de áreas aleatório a partir
# de uma seed

import csv
import random

max = 45.0
min = 75.0
numero_de_areas = 2000
random.seed(a=2)

# As áreas estão entre min mm^2 e max mm^2
with open('areas24.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['area_id', *['area{0}'.format(x) for x in range(1,25)]])
    for i in range(numero_de_areas):
        nums = [i]
        for j in range(24):
            num = random.random() * (max - min) + min
            nums.append(num)
        writer.writerow((str(x) for x in nums))
