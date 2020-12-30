import math
from math import sqrt, asin, acos, pi

################################################################################
## Class Triangulo
################################################################################

class Triangulo:

    def __init__(self, sideA=0.0, sideB=0.0, sideC=0.0):
        """
        Inicializa un objeto clase Triangulo.
        """
        # este código puede estar dentro de una condicion
        self.__sideA = 0.0
        self.__sideB = 0.0
        self.__sideC = 0.0
        self.__valid = False
        ladoa=round(float(sideA),1)
        ladob=round(float(sideB),1)
        ladoc=round(float(sideC),1)



        if(ladoa>0):
            self.__sideA=ladoa
        else:
            self.__sideA=0



        if (ladob > 0):
            self.__sideB = ladob
        else:
            self.__sideB = 0

        if (ladoc > 0):
            self.__sideC = ladoc
        else:
                self.__sideC = 0





    def __validate(self):

      if self.__sideA+self.__sideB>self.__sideC and self.__sideA+self.__sideC>self.__sideB and self.__sideB+self.__sideC>self.__sideA:
          return  True
      else:    return False





    def __repr__(self):

        a = str(self.__sideA)
        b = str(self.__sideB)
        c = str(self.__sideC)

        cadena = (a, b, c)
        return cadena

    def is_valid(self):



         if self.__sideA+self.__sideB>self.__sideC and self.__sideA+self.__sideC>self.__sideB and self.__sideB+self.__sideC>self.__sideA:
           return  True




    def is_equilateral(self):

        if(self.__sideA==self.__sideB==self.__sideC):
            return True



    def is_isosceles(self):
        if(self.__sideA==self.__sideB or self.__sideA==self.__sideC or self.__sideB==self.__sideC):
            return True




    def is_scalene(self):

        if(self.__sideA!=self.__sideB or self.__sideA!=self.__sideC or self.__sideB!=self.__sideC):
            return True


    def sides(self):

        tuplaLADOS=(self.__sideA,self.__sideB,self.__sideC)
        return tuplaLADOS

    def angles(self):

        anC = round((180/pi)*acos((pow(self.__sideA, 2) + pow(self.__sideB, 2) -pow(self.__sideC, 2))  / (2 * self.__sideA *self.__sideB)),1)
        anB = round((180/pi)*acos((pow(self.__sideA, 2) + pow(self.__sideC, 2) - pow(self.__sideB, 2)) / (2 * self.__sideA * self.__sideC)),1)
        anA = round((180/pi)*acos((pow(self.__sideB, 2) + pow(self.__sideC, 2) - pow(self.__sideA, 2)) / (2 * self.__sideB * self.__sideC)),1)
        tuplaAngulos = (anA,anB,anC)
        return tuplaAngulos





    def perimeter(self):

        s=self.__sideA+self.__sideB+self.__sideC

        return s

    def area(self):

        s=(self.__sideA+self.__sideB+self.__sideC)/2
        area=(s*(s-self.__sideA)*(s-self.__sideB)*(s-self.__sideC))**0.5
        return area




    def scale(self, factor=2.0):

       escala=(factor*self.__sideA,factor*self.__sideB,factor*self.__sideC)
       return escala


import random

random.seed(2020)
with open("triangulos.csv", mode='w') as file:
    file.write("LADO1,LADO2,LADO3\n")
    for _ in range(500):
        a = random.uniform(0, 100)
        b = random.uniform(0, 100)
        c = random.uniform(0, 100)
        file.write(f"{a},{b},{c}\n")

import  csv

validos = 0
sumPer=0
sumArea=0
periMayor=0
areaMayor=0
perTriaAreaMayor=0

triaPeriMayor=()
triaAreaMayor=()


with open( 'triangulos.csv') as f:
    f.readline()
    reader=csv.reader(f)
    
    listaobjetos=[]


    for row in reader:

        a=row[0]
        b=row[1]
        c=row[2]
        t=Triangulo(a,b,c)
        if(t.is_valid()):
            listaobjetos.append(t)

    for z in listaobjetos:
        if(z.is_valid()):
            validos=validos+1
            sumPer= sumPer+z.perimeter()
            sumArea=sumArea+z.area()
    for z in listaobjetos:
        if (z.is_valid()):
            if(z.perimeter()>periMayor):
                periMayor=z.perimeter();
                triaPeriMayor=z.__repr__()
                areaTriaPeriMayor=z.area()

    for k in listaobjetos:
        if (z.is_valid()):
            if (k.area() > areaMayor):
                areaMayor = k.area();
                triaAreaMayor = k.__repr__()
                perTriaAreaMayor = k.perimeter()

    promPer=sumPer/len(listaobjetos)
    promArea=sumArea/len(listaobjetos)




# Se define un triangulo valido
t = Triangulo(-2, 3, 3)

# Se muestran los datos del triangulo
print("Triangulo:", t.__repr__())
print("Es un triangulo valido:", t.is_valid())
print("Mulitplicado por un escalar", t.scale())
print("Es iscoles ?:", t.is_isosceles())
print("Es equilatero ? :", t.is_equilateral())
print("sides :", t.sides())
print("angulos en grados sexagesiames :", t.angles())
print("Perimetro del triangulo:", t.perimeter())
print("Area del triangulo:", t.area())
print("Es escaleno ? :", t.is_scalene())

print("1.numero de trinangulos validos sobre el total", validos)
print("2.perimetro promedio de los triangulos validos", promPer)
print("3.area promedio de los triangulos validos", promArea)
print("4.triangulo con mayor perimetro:", triaPeriMayor, "su perimetro: ", periMayor, " su area: ", areaTriaPeriMayor)
print("5.triangulo con mayor area: ", triaAreaMayor, "su perimetro: ", perTriaAreaMayor, "su area:", areaMayor)

#continuar con el código.