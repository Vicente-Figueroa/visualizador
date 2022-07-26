csvfile = open('./analisis/data/matriculas_2017.csv', 'r', encoding="utf8").readlines()
filename = 1
for i in range(len(csvfile)):
    if i % 10000 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+10000])
        filename += 1
