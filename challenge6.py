import random 

def average(lis: list):
    avg_hole_sizes = sum(lis)/len(lis)
    return avg_hole_sizes

def average_cost(lis: list):
    cost = 0
    for size in lis:
        if size < 20: cost += 1.30
        elif size >= 20 and size < 70: cost += 1.60
        else: cost += 2.10
    
    avg_cost = cost/100
    return avg_cost

def total_cost(lis: list):
    cost = 0
    for size in lis:
        if size < 20: cost += 1.30
        elif size >= 20 and size < 70: cost += 1.60
        else: cost += 2.10
    
    return cost

random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

print(hole_sizes)
# hole sizes in mm
hole_sizes[:5]

print(average(hole_sizes), "{:.3f}".format(round(average_cost(hole_sizes), 3)), total_cost(hole_sizes))

