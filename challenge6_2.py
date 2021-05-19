import random
import pandas as pd
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
hole_sizes[:5]

series = pd.Series(hole_sizes)
print(series.mean())

count_small, count_med, count_large = 0, 0, 0

for i in hole_sizes:
    if i < 20:
        count_small += 1
    elif i > 70:
        count_large += 1
    else:
        count_med += 1

average_cost = ((count_small*1.3)+(count_med*1.6)+(count_large*2.1))/100
print(average_cost)

total_cost = (count_small*1.3)+(count_med*1.6)+(count_large*2.1)
print(total_cost)