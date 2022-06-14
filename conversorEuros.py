euros = input("Cuantos euros tienes?: ")
euros = float(euros)
valorPesos = 0.000245607
pesos = euros / valorPesos
pesos = round(pesos, 2)
pesos = str(pesos)
print ("Tienes $" + pesos + " pesos") 


