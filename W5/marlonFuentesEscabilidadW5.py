#Tserial = n( microsegundos)
#Tparalelo =n/p+log2(p)
#speedup
#eficiencia 
#dominio y nucleos creciente 
import math
import pandas as pd 

dominio=[]
contador=0

#dominio a 320 
while contador<=320:
    contador=contador+10
    dominio.append(contador)

#nucleos 
nucleos=[1,2,4,8,16,32]

list_speed=[]
list_efficiency=[]
list_escability=[]

for p in nucleos:
    for n in dominio:
        lol_speed=[]
        lol_efficiency=[]
        lol_escability=[]

        lol_speed.append(p)
        lol_efficiency.append(p)
        lol_escability.append(p)


        lol_speed.append(n)
        lol_efficiency.append(n)
        lol_escability.append(n)

        Tserial=n
        Tparalelo=Tserial/p+math.log(p,2)
        Speedup=Tserial/Tparalelo
        Eficiencia=Tserial/(p*Speedup)
        lol_speed.append(Speedup)
        lol_efficiency.append(Eficiencia)
        list_speed.append(lol_speed)
        list_efficiency.append(lol_efficiency)

        division = math.log(p,2)
        if division != 0:                        
            k = ((n/Eficiencia)-n)/division            
            lol_escability.append(k)
            list_escability.append(lol_escability)


print(list_speed)
speedup_df=pd.DataFrame.from_records(list_speed)
print(list_efficiency)
efficiency_df=pd.DataFrame.from_records(list_efficiency)
print(list_escability)
escability_df=pd.DataFrame.from_records(list_escability)

speedup_df.columns=['nucleo','dominio','speedup']
efficiency_df.columns=['nucleo','dominio','efficiency']
escability_df.columns=['nucleo','dominio','escability']


speedup_df.to_csv("./speedup.csv", sep=";", index=False)
efficiency_df.to_csv("./efficiency.csv", sep=";", index=False)
escability_df.to_csv("./escability.csv", sep=";", index=False)