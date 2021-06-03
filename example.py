d_1, d_2, d_3 = 0, 0, 0
counter = 0

with open('dataset_3363_4.txt') as inf, open('out.txt', 'w') as ouf:
    for i in inf:
        b = i.strip().split(';')
        b[1], b[2], b[3] = int(b[1]), int(b[2]), int(b[3])
        ouf.write(str(sum([b[1], b[2], b[3]]) / 3) + '\n')
        d_1 += b[1]; d_2 += b[2]; d_3 += b[3]
        counter += 1
    s = str(d_1 / counter) + ' ' + str(d_2 / counter) + ' ' + str(d_3 / counter)
    ouf.write(s)

"""
st = [x.split(';') for x in open('fl.txt').readlines()]
print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
"""