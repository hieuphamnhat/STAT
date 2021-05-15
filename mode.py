import numpy as np
def calculateMode(x):
    index = 0
    x = np.sort(x)
    frq = []
    while index < len(x):
        x_tmp = x[index]
        count = 0
        for ele in x:
            if ele == x_tmp:
                count = count + 1
        frq.append(count)
        count = 0
        index = index + 1
    f_max = np.argmax(frq)
    return x, frq, f_max, x[f_max]

print(calculateMode(np.array([1,2,3,3])))
