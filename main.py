#===========Bibliotecas============

import math
print(math.factorial(6))
print('\n\n')

#=============Dicionários===========

classe = {"Ana": 4.5,
           "Beatriz": 6.5,
           "Geraldo": 1.0,
           "José": 10.0,
           "Maria": 9.5}
notas = classe.values()
média = sum(notas)/5
print("A média da classe é ",média)
print('\n\n')

dic = {"Salgado": 4.50, 
       "Lanche": 6.50, 
       "Suco": 3.00,
       "Refrigerante": 3.50, 
       "Doce": 1.00}
print(dic)
print('\n\n')


D = {"arroz": 17.30,"fejão": 12.50,"carne": 23.90,"alface": 3.40}
print(D)

D["carne"] = 25.0
D["tomate"] = 8.80
print(D)
print('\n\n')

#=========Praticando desenpacotamento==========

T =  (10,20,30,40,50)
a,b,c,d,e = T
print("a =",a,"b =",b)
print("d + e =",d+e)
print('\n\n')

#==========praticando com lista==============

L = [5, 7, 2, 9, 4, 1, 3]
print("Lista = ",L)
print("O tamanho da lista é ",len(L))
print("O maior elemento da lista é ",max(L))
print("O menor elemento da lista é ",min(L))
print("A soma dos elementos da lista é ",sum(L))
L.sort()
print("Lista em ordem crescente: ",L)
L.reverse()
print("Lista em ordem decrescente: ",L) 