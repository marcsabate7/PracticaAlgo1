import csv
from Bio import SeqIO


def completeList():
    with open('sequences.csv','r') as seq_file:
        csv_reader = csv.DictReader(seq_file)

        list = []
        trobat = False

        for seq in csv_reader:
            for j in range(len(list)):
                if seq['Geo_Location'] == list[j][0]:
                    trobat = True
                    list[j][1].append(int(seq['Length']))
                    j = len(list)-1
            if trobat == False:
                list.append([seq['Geo_Location'],[int(seq['Length'])]])
            trobat = False
    return list



def arnGen(arr):
    for seq_record in SeqIO.parse("sequences2.fasta", "fasta"):
        for i in range(len(arr)):
            if arr[i][2]==seq_record.id:
                temp= str(seq_record.seq)
                if len(temp)>1000:
                    temp = temp[:1001]
                arr[i].append(temp)
    print(arr)



    

def accesionCalculator(list):
    #print(list)
    with open('sequences.csv','r') as seq_file:
        csv_reader = csv.DictReader(seq_file)

        for seq in csv_reader:
            for i in range(len(list)):
                if seq['Geo_Location']==list[i][0] and int(seq['Length'])==list[i][1]:
                    list[i].append(seq['Accession'])   
                while len(list[i]) >=4:
                    list[i].pop()
    return list


def modify(list):
    for i in range(len(list)):
        list[i][1].sort()
    
    return list


def calculMediana(arr):
    list = []
    for i in range(len(arr)):
        long = len(arr[i][1])
        if long % 2 != 0:
            num = arr[i][1][int(round(long/2))-1]
        else:
            num = arr[i][1][int((long/2)+1)-1]
        total = 0
        list.append([arr[i][0],num])
    
    accesList = accesionCalculator(list)
    return accesList
    

if __name__=="__main__":
    list = completeList()
    arr = modify(list)
    accesList = calculMediana(arr)
    arnGen(accesList)
