# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:19:12 2021

@author: End User
"""

def anova(datos):
    Yidot=[]
    Yidot2=[]
    Yij2=[]
    for i in range(len(datos)):
        Yidot.append(sum(datos[i]))
        Yidot2.append((sum(datos[i]))**2)
    Ydotdot=sum(Yidot)
    SYidot2=sum(Yidot2) 
    i=0
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            Yij2.append((datos[i][j])**2)
    SYij2=sum(Yij2)
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
    return Fo

    
            
    
        
    