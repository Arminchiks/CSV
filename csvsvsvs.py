import csv

with open('irv100_04.csv', 'r', encoding= 'utf-8') as file:
    csv1=csv.reader(file)
    saraksts = list(csv1)
    reader=csv.DictReader(file)

    print("Izdruka ir", saraksts)
    print("\n")

    #print(sorted(saraksts,reverse=True))
first = saraksts[1]
print("Pirmais elements sarakstā ir: ", first, '\n')

last=saraksts[-1]
print("Pedejais elements: ", last, "\n")

Third_last=saraksts[-3]
print("Tresais no beigām", Third_last,'\n')

p_pieci=saraksts[1:5]
print("Pirmais lidz piektais ir:", p_pieci, '\n')


#def nosaukums():
#    print("Faila nosaukums:", file.name, "\n")


    


