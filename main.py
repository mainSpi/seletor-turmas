import csv
from openpyxl import Workbook
from openpyxl.styles import Font

lugares = {
    "Heitor Beltrão": 8,
    "João Barros Neto" : 10,
    "Hesfa/Marcolino" : 12,
    "Estácio de Sá" : 10,
    "Felippe Cardoso" : 12
}

turmas = ["t1.csv", "t2.csv"]


turmas = {list(turmas)[i]: [] for i in range(len(turmas))} # cria um array vazio para cada turma

def salvarComoPlanilha():
    wb = Workbook()
    wb.remove(wb.active)
    for turma, divisao in turmas.items():
        ws = wb.create_sheet(turma)
        
        for lugar, alunos in divisao.items():
            coluna = list(divisao.keys()).index(lugar) + 1
            celulaLugar = ws.cell(row=1, column=coluna)
            celulaLugar.value = lugar
            celulaLugar.font = Font(color = "FF0000")

            for i in range(0, len(alunos)):
                ws.cell(row=i+2, column=coluna).value = alunos[i]

    wb.save("saida.xlsx")


for turma in turmas.keys():
    divisao = {list(lugares.keys())[i]: [] for i in range(len(lugares.keys()))} # # cria um array vazio para cada lugar
    
    with open(turma) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            prioridades = row[1:len(lugares.keys())+1] # vem umas colunas em branco que podem atrapalhar
            prioridades = list(map(int, prioridades)) # transformando em numero
            
            for i in range(1, len(lugares.keys()) + 1): # loopando sobre as prioridades ate achar
                index = prioridades.index(i)
                lugar = list(lugares.keys())[index]
                temVaga = True if len(divisao[lugar]) < lugares[lugar] else False
                if (temVaga):
                    divisao[lugar].append(row[0])
                    break # achou vaga, sai do loop
    turmas[turma] = divisao

salvarComoPlanilha()