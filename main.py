import csv
from xlwt import Workbook 

lugares = {
    "Heitor Beltrão": 8,
    "João Barros Neto" : 10,
    "Hesfa/Marcolino" : 12,
    "Estácio de Sá" : 10,
    "Felippe Cardoso" : 12
}

turmas = ["t1.csv", "t2.csv"]

def salvarComoPlanilha():
    pass


for turma in turmas:
    divisao = {} # "Heitor Beltrão": ["Fulano", "Cicrano", ...], "Felippe Cardoso" : ["Beltrano", ...]
    for l in lugares.keys():
        divisao[l] = [] # criando as chaves
    print(divisao)
    with open(turma) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            pass
            prioridades = row[1:len(lugares.keys())+1] # vem umas colunas em branco que podem atrapalhar
            prioridades = list(map(int, prioridades)) # transformando em numero
            
            for i in range(1, len(lugares.keys()) + 1): # loopando sobre as prioridades ate achar
                index = prioridades.index(i)
                lugar = list(lugares.keys())[index]
                temVaga = True if len(divisao[lugar]) < lugares[lugar] else False
                if (temVaga):
                    divisao[lugar].append(row[0])
                    break # achou vaga, sai do loop
    print(divisao)
    salvarComoPlanilha()