def run():

    #Contador que itinera hasta el número de que se introduce en el for
     for contador in range(1000):
         if contador % 2 != 0:
             continue
         print(contador)
    
     for i in range(10000):
         print(i)
         if i == 5678:
             break

    #Se introduce una palabra y la devuelve hasta la letra o
     texto = input("Escribe un texto: ") 
     for letra in texto: 
         if letra == "o":
             break
         print(letra)



     LIMITE = 1000
     count = 0
     while count < 30:
         count += 1
         if count % 2 != 0:
             print("este numero es impar " + str(count))
             continue
         else:
             print("este numero es par " + str(count))
             
if __name__ == "__main__":
    
    run()