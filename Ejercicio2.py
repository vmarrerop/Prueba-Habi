def counts(equipoA, equipoB):
    res = []
    
    for b in equipoB:
        count = 0
        for a in equipoA:
            if a <= b:
                count += 1
        res.append(count)
    
    return res

equipoA = [2, 10, 5, 4, 8]
equipoB = [3, 1, 7, 8]
res = counts(equipoA, equipoB)
print(res)