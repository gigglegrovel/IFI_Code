
#%%
from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing
import random
import time




p = pd.read_excel("C:/Users/End User/Documents/Machine Learning/Final_dataset.xlsx")

p.pop('Unnamed: 0')

for i in range(len(p["property_type"])):
    if p["property_type"][i]=="Departamento":
        p["property_type"][i]=0
    if p["property_type"][i]=="Casa":
        p["property_type"][i]=1

for i in range(len(p['operation_type'])):
    if p['operation_type'][i]=="Renta":
        p['operation_type'][i]=0
    if p['operation_type'][i]=="venta":
        p['operation_type'][i]=1

for i in range(len(p['due_date'])):
    p['due_date'][i]=int(p['due_date'][i].replace('-',''))

data = p

venta = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
renta = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
for i in range(len(p['operation_type'])):
    if p['operation_type'][i]==0:
        renta['price'].append(p['price'][i])
        renta['built_floor_area'].append(p['built_floor_area'][i])
        renta['bathrooms'].append(p['bathrooms'][i])
        renta['rooms'].append(p['rooms'][i])
        renta['property_type'].append(p['property_type'][i])
        renta['garage'].append(p['garage'][i])
    elif p['operation_type'][i]==1:
        venta['price'].append(p['price'][i])
        venta['built_floor_area'].append(p['built_floor_area'][i])
        venta['bathrooms'].append(p['bathrooms'][i])
        venta['rooms'].append(p['rooms'][i])
        venta['property_type'].append(p['property_type'][i])
        venta['garage'].append(p['garage'][i])


renta_v=[]
venta_v=[]

for i in range(len(venta['price'])):
    venta_v.append([1,venta['built_floor_area'][i],venta['rooms'][i]])


for i in range(len(renta['price'])):
    renta_v.append([1,renta['built_floor_area'][i],renta['rooms'][i]])
    
venta_v = np.array(venta_v)
renta_v = np.array(renta_v)

venta_v.reshape((len(venta['price']),3))
renta_v.reshape((len(renta['price']),3))

scaled_renta = preprocessing.scale(renta_v, axis=0, with_mean=True, with_std=True, copy=True)
scaled_venta = preprocessing.scale(venta_v, axis=0, with_mean=True, with_std=True, copy=True)


vrooms1 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
vrooms2 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
vrooms3 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}

vrooms4 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
vrooms5 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}

rrooms1 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
rrooms2 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
rrooms3 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}

rrooms4 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}
rrooms5 = {'price':[],'built_floor_area':[],'bathrooms':[],'rooms':[],'property_type':[],'garage':[]}

for i in range(len(venta['price'])):
    if venta['rooms'][i]==1:
        vrooms1['price'].append(venta['price'][i])
        vrooms1['built_floor_area'].append(venta['built_floor_area'][i])
        vrooms1['bathrooms'].append(venta['bathrooms'][i])
        vrooms1['rooms'].append(venta['rooms'][i])
        vrooms1['property_type'].append(venta['property_type'][i])
        vrooms1['garage'].append(venta['garage'][i])
    elif venta['rooms'][i]==2:
        vrooms2['price'].append(venta['price'][i])
        vrooms2['built_floor_area'].append(venta['built_floor_area'][i])
        vrooms2['bathrooms'].append(venta['bathrooms'][i])
        vrooms2['rooms'].append(venta['rooms'][i])
        vrooms2['property_type'].append(venta['property_type'][i])
        vrooms2['garage'].append(venta['garage'][i])
    elif venta['rooms'][i]==3:
        vrooms3['price'].append(venta['price'][i])
        vrooms3['built_floor_area'].append(venta['built_floor_area'][i])
        vrooms3['bathrooms'].append(venta['bathrooms'][i])
        vrooms3['rooms'].append(venta['rooms'][i])
        vrooms3['property_type'].append(venta['property_type'][i])
        vrooms3['garage'].append(venta['garage'][i])
    elif venta['rooms'][i]==4:
        vrooms4['price'].append(venta['price'][i])
        vrooms4['built_floor_area'].append(venta['built_floor_area'][i])
        vrooms4['bathrooms'].append(venta['bathrooms'][i])
        vrooms4['rooms'].append(venta['rooms'][i])
        vrooms4['property_type'].append(venta['property_type'][i])
        vrooms4['garage'].append(venta['garage'][i])
    else:
        vrooms5['price'].append(venta['price'][i])
        vrooms5['built_floor_area'].append(venta['built_floor_area'][i])
        vrooms5['bathrooms'].append(venta['bathrooms'][i])
        vrooms5['rooms'].append(venta['rooms'][i])
        vrooms5['property_type'].append(venta['property_type'][i])
        vrooms5['garage'].append(venta['garage'][i])

for i in range(len(renta['price'])):
    if renta['rooms'][i]==1:
        rrooms1['price'].append(renta['price'][i])
        rrooms1['built_floor_area'].append(renta['built_floor_area'][i])
        rrooms1['bathrooms'].append(renta['bathrooms'][i])
        rrooms1['rooms'].append(renta['rooms'][i])
        rrooms1['property_type'].append(renta['property_type'][i])
        rrooms1['garage'].append(renta['garage'][i])
    elif renta['rooms'][i]==2:
        rrooms2['price'].append(renta['price'][i])
        rrooms2['built_floor_area'].append(renta['built_floor_area'][i])
        rrooms2['bathrooms'].append(renta['bathrooms'][i])
        rrooms2['rooms'].append(renta['rooms'][i])
        rrooms2['property_type'].append(renta['property_type'][i])
        rrooms2['garage'].append(renta['garage'][i])
    elif renta['rooms'][i]==3:
        rrooms3['price'].append(renta['price'][i])
        rrooms3['built_floor_area'].append(renta['built_floor_area'][i])
        rrooms3['bathrooms'].append(renta['bathrooms'][i])
        rrooms3['rooms'].append(renta['rooms'][i])
        rrooms3['property_type'].append(renta['property_type'][i])
        rrooms3['garage'].append(renta['garage'][i])
    elif renta['rooms'][i]==4:
        rrooms4['price'].append(renta['price'][i])
        rrooms4['built_floor_area'].append(renta['built_floor_area'][i])
        rrooms4['bathrooms'].append(renta['bathrooms'][i])
        rrooms4['rooms'].append(renta['rooms'][i])
        rrooms4['property_type'].append(renta['property_type'][i])
        rrooms4['garage'].append(renta['garage'][i])
    else:
        rrooms5['price'].append(renta['price'][i])
        rrooms5['built_floor_area'].append(renta['built_floor_area'][i])
        rrooms5['bathrooms'].append(renta['bathrooms'][i])
        rrooms5['rooms'].append(renta['rooms'][i])
        rrooms5['property_type'].append(renta['property_type'][i])
        rrooms5['garage'].append(renta['garage'][i])
#Ventas
chisk = []
result = []
contendents = []
pedri = []
pedri2 = []
peluca = {'price':list(venta['price']),'built_floor_area':list(venta['built_floor_area']),'rooms':list(venta['rooms'])}
for k in range(10):
    print('Outerfold '+str(k+1))
    venta = {'price':list(peluca['price']),'built_floor_area':list(peluca['built_floor_area']),'rooms':list(peluca['rooms'])}
    
    for i in range(4):
        venta['price'].pop(41-4*k-i)
        venta['built_floor_area'].pop(41-4*k-i)
        venta['rooms'].pop(41-4*k-i)
        
    numbers = list(range(1,42))
    
    Vp1 = list(venta['price'])
    Vpp1=[]
    Va1 = list(venta['built_floor_area'])
    Vaa1=[]
    Vh1 = list(venta['rooms'])
    Vhh1=[]
    rand1 = numbers[0:3]
    
    Vp2 = list(venta['price'])
    Vpp2=[]
    Va2 = list(venta['built_floor_area'])
    Vaa2=[]
    Vh2 = list(venta['rooms'])
    Vhh2=[]
    rand2 = numbers[3:6]
    
    Vp3 = list(venta['price'])
    Vpp3=[]
    Va3 = list(venta['built_floor_area'])
    Vaa3=[]
    Vh3 = list(venta['rooms'])
    Vhh3=[]
    rand3 = numbers[6:9]
    
    Va4 = list(venta['built_floor_area'])
    Vp4 = list(venta['price'])
    Vpp4=[]
    Vaa4=[]
    Vh4 = list(venta['rooms'])
    Vhh4=[]
    rand4 = numbers[9:12]
    
    Va5 = list(venta['built_floor_area'])
    Vp5 = list(venta['price'])
    Vpp5=[]
    Vaa5=[]
    Vh5 = list(venta['rooms'])
    Vhh5=[]
    rand5 = numbers[12:15]
    
    Va6 = list(venta['built_floor_area'])
    Vp6 = list(venta['price'])
    Vaa6=[]
    Vpp6=[]
    Vh6 = list(venta['rooms'])
    Vhh6=[]
    rand6 = numbers[15:18]
    
    Va7 = list(venta['built_floor_area'])
    Vp7 = list(venta['price'])
    Vpp7=[]
    Vaa7=[]
    Vh7 = list(venta['rooms'])
    Vhh7=[]
    rand7 = numbers[18:21]
    
    Va8 = list(venta['built_floor_area'])
    Vp8 = list(venta['price'])
    Vpp8=[]
    Vaa8=[]
    Vh8 = list(venta['rooms'])
    Vhh8=[]
    rand8 = numbers[21:24]
    
    Va9 = list(venta['built_floor_area'])
    Vp9 = list(venta['price'])
    Vpp9=[]
    Vaa9=[]
    Vh9 = list(venta['rooms'])
    Vhh9=[]
    rand9 = numbers[24:27]
    
    
    Va10 = list(venta['built_floor_area'])
    Vp10 = list(venta['price'])
    Vpp10=[]
    Vaa10=[]
    Vh10 = list(venta['rooms'])
    Vhh10=[]
    rand10 = numbers[27:30]
    
    for i in range(3):    
        Vpp1.append(Vp1[rand1[i]])
        Vaa1.append(Va1[rand1[i]])
        Vhh1.append(Vh1[rand1[i]])
        Vp1.pop(rand1[i])
        Va1.pop(rand1[i])
        Vh1.pop(rand1[i])
    for i in range(3):
        Vpp2.append(Vp2[rand2[i]])
        Vaa2.append(Va2[rand2[i]])
        Vhh2.append(Vh2[rand2[i]])
        Vp2.pop(rand2[i])
        Va2.pop(rand2[i])
        Vh2.pop(rand2[i])
    for i in range(3):
        Vpp3.append(Vp3[rand3[i]])
        Vaa3.append(Va3[rand3[i]])
        Vhh3.append(Vh3[rand3[i]])
        Vp3.pop(rand3[i])
        Va3.pop(rand3[i])
        Vh3.pop(rand3[i])
    
    for i in range(3):
        Vpp4.append(Vp4[rand4[i]])
        Vaa4.append(Va4[rand4[i]])
        Vhh4.append(Vh4[rand4[i]])
        Vp4.pop(rand4[i])
        Va4.pop(rand4[i])
        Vh4.pop(rand4[i])
        
    for i in range(3):
        Vpp5.append(Vp5[rand5[i]])
        Vaa5.append(Va5[rand5[i]])
        Vhh5.append(Vh5[rand5[i]])
        Vp5.pop(rand5[i])
        Va5.pop(rand5[i])
        Vh5.pop(rand5[i])
        
    for i in range(3):
        Vpp6.append(Vp6[rand6[i]])
        Vaa6.append(Va6[rand6[i]])
        Vhh6.append(Vh6[rand6[i]])
        Vp6.pop(rand6[i])
        Va6.pop(rand6[i])
        Vh6.pop(rand6[i])
    
    for i in range(3):
        Vpp7.append(Vp7[rand7[i]])
        Vaa7.append(Va7[rand7[i]])
        Vhh7.append(Vh7[rand7[i]])
        Vp7.pop(rand7[i])
        Va7.pop(rand7[i])
        Vh7.pop(rand7[i])
    
    for i in range(3):
        Vpp8.append(Vp8[rand8[i]])
        Vaa8.append(Va8[rand8[i]])
        Vhh8.append(Vh8[rand8[i]])
        Vp8.pop(rand8[i])
        Va8.pop(rand8[i])
        Vh8.pop(rand8[i])
    
    for i in range(3):
        Vpp9.append(Vp9[rand9[i]])
        Vaa9.append(Va9[rand9[i]])
        Vhh9.append(Vh9[rand9[i]])
        Vp9.pop(rand9[i])
        Va9.pop(rand9[i])
        Vh9.pop(rand9[i])
    
    for i in range(3):
        Vpp10.append(Vp10[rand10[i]])
        Vaa10.append(Va10[rand10[i]])
        Vhh10.append(Vh10[rand10[i]])
        Vp10.pop(rand10[i])
        Va10.pop(rand10[i])
        Vh10.pop(rand10[i])
        
    
    
    lambdar = [.0001,.001,.01,.1,1,10,100,1000,10000,100000,1000000]
    
    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []
    X6 = []
    X7 = []
    X8 = []
    X9 = []
    X10 = []
    
    for i in range(len(Vp1)):
        X1.append([1,Va1[i],Vh1[i]])
    for i in range(len(Vp2)):
        X2.append([1,Va2[i],Vh2[i]])
    for i in range(len(Vp3)):
        X3.append([1,Va3[i],Vh3[i]])
    for i in range(len(Vp1)):
        X4.append([1,Va4[i],Vh4[i]])
    for i in range(len(Vp5)):
        X5.append([1,Va5[i],Vh5[i]])
    for i in range(len(Vp1)):
        X6.append([1,Va6[i],Vh6[i]])
    for i in range(len(Vp1)):
        X7.append([1,Va7[i],Vh7[i]])
    for i in range(len(Vp1)):
        X8.append([1,Va8[i],Vh8[i]])
    for i in range(len(Vp1)):
        X9.append([1,Va9[i],Vh9[i]])
    for i in range(len(Vp1)):
        X10.append([1,Va10[i],Vh10[i]])
    
    
    X1 = np.array(X1)
    
    X2 = np.array(X2)
    
    X3 = np.array(X3)
    
    X4 = np.array(X1)
    
    X5 = np.array(X5)
    
    X6 = np.array(X6)
    
    X7 = np.array(X7)
    
    X8 = np.array(X8)
    
    X9 = np.array(X9)
    
    X10 = np.array(X10)
    
    W1 = []
    
    W2 = []
    
    W3 = []
    
    W4 = []
    
    W5 = []
    
    W6 = []
    
    W7 = []
    
    W8 = []
    
    W9 = []
    
    W10 = []
    
    X1 = preprocessing.scale(X1, axis=0, with_mean=True, with_std=True, copy=True)
    
    X2 = preprocessing.scale(X2, axis=0, with_mean=True, with_std=True, copy=True)
    
    X3 = preprocessing.scale(X3, axis=0, with_mean=True, with_std=True, copy=True)
    
    X4 = preprocessing.scale(X4, axis=0, with_mean=True, with_std=True, copy=True)
    
    X5 = preprocessing.scale(X5, axis=0, with_mean=True, with_std=True, copy=True)
    
    X6 = preprocessing.scale(X6, axis=0, with_mean=True, with_std=True, copy=True)
    
    X7 = preprocessing.scale(X7, axis=0, with_mean=True, with_std=True, copy=True)
    
    X8 = preprocessing.scale(X8, axis=0, with_mean=True, with_std=True, copy=True)
    
    X9 = preprocessing.scale(X9, axis=0, with_mean=True, with_std=True, copy=True)
    
    X10 = preprocessing.scale(X10, axis=0, with_mean=True, with_std=True, copy=True)
    
    
    
    for m in range(len(lambdar)):

        W1.append(np.dot(np.dot(np.linalg.inv(np.dot(X1.T,X1)+lambdar[m]*np.identity(3)),X1.T),Vp1))
        W2.append(np.dot(np.dot(np.linalg.inv(np.dot(X2.T,X2)+lambdar[m]*np.identity(3)),X2.T),Vp2))
        W3.append(np.dot(np.dot(np.linalg.inv(np.dot(X3.T,X3)+lambdar[m]*np.identity(3)),X3.T),Vp3))
        W4.append(np.dot(np.dot(np.linalg.inv(np.dot(X4.T,X4)+lambdar[m]*np.identity(3)),X4.T),Vp4))
        W5.append(np.dot(np.dot(np.linalg.inv(np.dot(X5.T,X5)+lambdar[m]*np.identity(3)),X5.T),Vp5))
        W6.append(np.dot(np.dot(np.linalg.inv(np.dot(X6.T,X6)+lambdar[m]*np.identity(3)),X6.T),Vp6))
        W7.append(np.dot(np.dot(np.linalg.inv(np.dot(X7.T,X7)+lambdar[m]*np.identity(3)),X7.T),Vp7))
        W8.append(np.dot(np.dot(np.linalg.inv(np.dot(X8.T,X8)+lambdar[m]*np.identity(3)),X8.T),Vp8))
        W9.append(np.dot(np.dot(np.linalg.inv(np.dot(X9.T,X9)+lambdar[m]*np.identity(3)),X9.T),Vp9))
        W10.append(np.dot(np.dot(np.linalg.inv(np.dot(X10.T,X10)+lambdar[m]*np.identity(3)),X10.T),Vp10))
            
        if m==len(lambdar)-1:
            lower = 0
            location = [1,1]
           # print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W1[i],W1[i])
                for j in range(len(Vpp1)):
                    Error+=(Vpp1[j]-W1[i][0]-W1[i][1]*Vaa1[j]-W1[i][2]*Vhh1[j])**2      
                    if j == 1:
                        lower = Error
                        minor = W1[j]
                        pedri = W1
                    if j>1 and Error<lower:
                        minor=W1[j]
                        pedri = W1
                        lower = Error
                        location[0]=1
                        location[1]=j
           #     print(str(1)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
           # print('Innerfold \t Lambda \t Error')
            
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W2[i],W2[i])
                for j in range(len(Vpp2)):
                    Error+=(Vpp2[j]-W2[i][0]-W2[i][1]*Vaa2[j]-W2[i][2]*Vhh2[j])**2
                    if Error<lower:
                       minor=W2[j]
                       lower = Error
                       location[0]=2
                       location[1]=j
                       pedri = W2
            #    print(str(2)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
          
           # print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W3[i],W3[i])
                for j in range(len(Vpp3)):
                    Error+=(Vpp3[j]-W3[i][0]-W3[i][1]*Vaa3[j]-W3[i][2]*Vhh3[j])**2 
                    if Error<lower:
                       minor=W3[j] 
                       lower = Error
                       location[0]=3
                       location[1]=j
                       pedri = W3
            #    print(str(3)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W4[i],W4[i])
                for j in range(len(Vpp4)):
                    Error+=(Vpp4[j]-W4[i][0]-W4[i][1]*Vaa4[j]-W4[i][2]*Vhh4[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=4
                       location[1]=j
                       minor=W4[j]
                       pedri = W4
             #   print(str(4)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W5[i],W5[i])
                for j in range(len(Vpp5)):
                    Error+=(Vpp5[j]-W5[i][0]-W5[i][1]*Vaa5[j]-W5[i][2]*Vhh5[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=5
                       location[1]=j
                       minor=W5[j]
                       pedri = W5
             #   print(str(5)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W6[i],W6[i])
                for j in range(len(Vpp6)):
                    Error+=(Vpp6[j]-W6[i][0]-W6[i][1]*Vaa6[j]-W6[i][2]*Vhh6[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=6
                       location[1]=j
                       pedri = W6
             #   print(str(6)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W7[i],W7[i])
                for j in range(len(Vpp7)):
                    Error+=(Vpp7[j]-W7[i][0]-W7[i][1]*Vaa7[j]-W7[i][2]*Vhh7[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=7
                       location[1]=j
                       pedri = W7
             #   print(str(7)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W8[i],W8[i])
                for j in range(len(Vpp8)):
                    Error+=(Vpp8[j]-W8[i][0]-W8[i][1]*Vaa8[j]-W8[i][2]*Vhh8[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=8
                       location[1]=j
                       pedri = W8
             #   print(str(8)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W9[i],W9[i])
                for j in range(len(Vpp9)):
                    Error+=(Vpp9[j]-W9[i][0]-W9[i][1]*Vaa9[j]-W9[i][2]*Vhh9[j])**2
                    if Error<lower:
                       lower = Error
                       location[0]=9
                       location[1]=j
                       pedri = W9
             #   print(str(9)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
        
            #print('Innerfold \t Lambda \t Error')
            for i in range(len(lambdar)):
                Error = lambdar[i]*np.dot(W10[i],W10[i])
                for j in range(len(Vpp10)):
                    Error+=(Vpp10[j]-W10[i][0]-W10[i][1]*Vaa10[j]-W10[i][2]*Vhh10[j])**2 
                    if Error<lower:
                       lower = Error
                       location[0]=10
                       location[1]=j
                       pedri = W10
             #   print(str(10)+'\t\t\t'+str(lambdar[i])+'\t\t\t'+str(Error))
    wvec = [0,W1,W2,W3,W4,W5,W6,W7,W8,W9,W10]
    contendents.append(wvec[location[0]][location[1]])
    chisk.append(minor)
    result.append([location,lower,k])
    pedri2.append(pedri)
    
    
#[    0.         18928.37137015 12677.35218327]

def shit():
    a = np.linspace(0,1500,10000)
    b = a*24304.6
    fig,axes = plt.subplots()
    axes.scatter( vrooms1['built_floor_area'],vrooms1['price'], s=10, c='b', marker="s",label='rooms=1')
    axes.scatter( vrooms2['built_floor_area'],vrooms2['price'], s=10, c='r', marker="o",label='rooms=2')
    axes.scatter( vrooms3['built_floor_area'],vrooms3['price'], s=10, c='c', marker="*",label='rooms=3')
    axes.scatter( vrooms4['built_floor_area'],vrooms4['price'], s=10, c='g', marker="+",label='rooms=4')
    axes.scatter( vrooms5['built_floor_area'],vrooms5['price'], s=10, c='m', marker="D",label='rooms=5')
    plt.legend(loc='lower right');
    colors = ['b','r','c','g','m']
    for i in range(5):
        plt.plot(a,b+(i+1)*(15292.1),colors[i])
    plt.show()
DefErr = []
for i in range(10):
    u = peluca['price'][(41-4*i-4):(41-4*i)]
    v = peluca['built_floor_area'][(41-4*i-4):(41-4*i)]
    vv = peluca['rooms'][(41-4*i-4):(41-4*i)]
    Error=0
    for j in range(len(u)):
        Error+=(u[j]-v[j]*chisk[i][1]-vv[j]*chisk[i][2])**2
    print(Error,i)
    
    
y = []
c = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(chisk)):
    for j in range(len(venta['price'])):
    c[i]+=np.exp(np.dot(chisk[i],[0,venta['built_floor_area'][j],venta['rooms'][j]]))
for i in range(len(chisk)):
    for j in range(len(venta['price'])):
        y.append(np.exp(np.dot(chisk[i],[0,venta['built_floor_area'][j],venta['rooms'][j]]))/(c[i]+1))
# %%
