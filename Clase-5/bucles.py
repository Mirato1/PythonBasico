def run():
    
    #Potencia de 2 hasta 1024
     LIMITE = 1025   

     contador = 0
     potencia_2 = 2**contador
     while potencia_2 < LIMITE:
         print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
         contador = contador + 1 
         potencia_2 = 2**contador


if __name__ == '__main__':
     run()

#Contador hasta 10
contador = 1
print(contador)
while contador < 10:
     contador += 1 
     print(contador)


for contador in range(11):
     print(contador)

for i in range(10):
    print(11 * i)
