#%%
import pandas as pd
#País a inspeccionar
pais="Uruguay"
#Leemos el documento
p=pd.read_csv('C:/Users/End User/Downloads/'+pais+".csv",header=0,encoding='latin-1')
#Lista de caracteres que se aceptan, incluyendo espacios ' y -
alf=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á','É','Í','Ó','Ú','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á','é','í','ó','ú',"'"," ",'ñ','.','1','2','3','4','5','6','7','8','9','0']
#Por cada elemento en la lista, vamos a generar una lista de caracteres
#que forman ese elemento, y si algun elemento no esta en nuestra lista 
#de caracteres aceptados, lo imprimimos
for i in range(len(p["nom_1"])):
    for j in range(len(list(p["nom_1"][i]))):
        if list(p["nom_1"][i])[j] not in alf:
            print("Palabra: "+p["nom_1"][i],"Caracter: "+list(p["nom_1"][i])[j],"Fila: "+str(i),"Columna: 1")

for i in range(len(p["nom_2"])):
    for j in range(len(list(p["nom_2"][i]))):
        if list(p["nom_2"][i])[j] not in alf:
            print("Palabra: "+p["nom_2"][i],"Caracter: "+list(p["nom_2"][i])[j],"Fila: "+str(i),"Columna: 2")

