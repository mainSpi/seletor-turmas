import csv

lugares = {
    "Heitor Beltrão": 8,
    "João Barros Neto" : 10,
    "Hesfa/Marcolino" : 12,
    "Estácio de Sá" : 10,
    "Felippe Cardoso" : 12
}

turmas = ["t1.csv", "t2.csv"]

with open("t1.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)