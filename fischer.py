# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:37:37 2021

@author: End User
"""
import math
def anova(datos):
    Yidot=[]
    Yidot2=[]
    Yij2=[]
    for i in range(len(datos)):
        Yidot.append(sum(datos[i]))
        Yidot2.append((sum(datos[i]))**2)
    Ydotdot=sum(Yidot)
    print(Ydotdot,'Ydotdot')
    SYidot2=sum(Yidot2) 
    print(SYidot2,'SYidot2')
    i=0
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            Yij2.append((datos[i][j])**2)
    SYij2=sum(Yij2)
    print(SYij2,'SYij2')
    SSt=SYij2-(Ydotdot**2)/(len(datos)*len(datos[0]))
    print('SStotal',SSt)
    SStr=SYidot2/len(datos[0])-(Ydotdot**2)/(len(datos)*len(datos[0]))
    print('SStratamiento',SStr)
    SSerror=SSt-SStr
    print('SSerror',SSerror)
    Ms_tr=SStr/(len(datos)-1)
    print('MsTratamiento',Ms_tr)
    Ms_error=SSerror/(len(datos)*len(datos[0])-len(datos))
    print('MsError',Ms_error)
    Fo=Ms_tr/Ms_error
    return Fo,Ms_error

def fischer(datos,t_a_2):
    av=[]
    Fo,Ms_error=anova(datos)
    for i in range(len(datos)):
        av.append(sum(datos[i])/len(datos[i]))
    LSD = t_a_2*math.sqrt((2*Ms_error)/len(datos[i]))    
    av.sort()
    i=0
    for i in range(len(av)):
        for j in range(i+1,len(av)):
            if av[j]-av[i]<LSD:
                print(av[i],av[j],'iguales')
            else:
                print(av[i],av[j],'diferentes')
    return av, LSD

def tuckey(datos,t):
    av=[]
    Fo,Ms_error=anova(datos)
    for i in range(len(datos)):
        av.append(sum(datos[i])/len(datos[i]))
    HSD = t*math.sqrt((Ms_error)/len(datos[0]))  
    print(HSD,'HSD')
    av.sort()
    i=0
    for i in range(len(av)):
        for j in range(i+1,len(av)):
            if av[j]-av[i]<HSD:
                print(av[i],av[j],'iguales')
            else:
                print(av[i],av[j],'diferentes')
    return av, HSD



def bloqueo(datos):
    Yidot=[]
    Yjdot=[]
    Yidot2=[]
    Yjdot2=[]
    Yij2=[]
    for i in range(len(datos)):
        Yidot.append(sum(datos[i]))
        Yidot2.append((sum(datos[i]))**2)
    Ydotdot=sum(Yidot)
    print(Ydotdot,'Ydotdot')
    SYidot2=sum(Yidot2) 
    print(SYidot2,'SYidot2')
    i=0
    for i in range(len(datos[0])):
        s=0
        for j in range(len(datos)):
            s+=datos[j][i]
        Yjdot.append(s)
        Yjdot2.append(s**2)
        j=0  
    SYjdot2=sum(Yjdot2) 
    print(SYjdot2,'SYjdtot')
    i=0
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            Yij2.append((datos[i][j])**2)
    SYij2=sum(Yij2)
    print(SYij2,'SYij2')
    SSt=SYij2-(Ydotdot**2)/(len(datos)*len(datos[0]))
    print('SStotal',SSt)
    SStr=SYidot2/len(datos[0])-(Ydotdot**2)/(len(datos)*len(datos[0]))
    print('SStratamiento',SStr)
    SSbloqueo = SYjdot2/len(datos)-(Ydotdot**2)/(len(datos)*len(datos[0]))
    print(SSbloqueo,'SSBloqueo')
    SSerror=SSt-SStr-SSbloqueo
    print('SSerror',SSerror)
    Ms_tr=SStr/(len(datos)-1)
    print('MsTratamiento',Ms_tr)
    Ms_error=SSerror/((len(datos)-1)*(len(datos[0])-1))
    print('MsError',Ms_error)
    Fo=Ms_tr/Ms_error
    return Fo,Ms_error    

