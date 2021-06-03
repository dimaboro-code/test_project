tall_dict = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: []
}
with open('dataset_3380_5.txt') as inf, open('out.txt', 'w') as ouf:
    for line in inf:
        d = line.strip().split()
        tall_dict[int(d[0])].append(int(d[2]))
    for i in range(1, 12):
        if len(tall_dict[i]) == 0:
            ouf.write(str(i) + ' -' + '\n')
        else:
            ouf.write(str(i) + ' ' + str(sum(tall_dict[i]) / len(tall_dict[i])) + '\n')
