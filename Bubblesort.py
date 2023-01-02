from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import timeit

tamanho = [1000, 2000, 3000, 4000, 5000, 8000, 11000, 15000]

def gerarLista(tam):
    lista = []
    while len(lista) < tam:
        x = randint(1,1*tam)
        if x not in lista: lista.append(x)
    return lista

def bubble_sort(lista):
  n= len(lista)
  for j in range(n-1):
    for i in range(n-1):
      if lista[i] > lista[i+1]:
        lista[i],lista[i+1] = lista[i+1], lista[i]
      

mpl.use('Agg')
def gerarGrafico(x,y,z):    
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Caso")
    ax.plot(x,z, label = "Pior Caso")    
    plt.xlabel('TAMANHO DA LISTA')
    plt.ylabel('TEMPO DE ORDENAMENTO') 
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    fig.savefig('graph.png')

Melhor_Caso = []
Pior_Caso = []

for i in tamanho:
  normal = gerarLista(i)
  melhor = sorted(normal)
  pior = sorted(normal, reverse=True)
  Melhor_Caso.append(timeit.timeit("bubble_sort({})".format(melhor),setup="from __main__ import bubble_sort",number=1))
  Pior_Caso.append(timeit.timeit("bubble_sort({})".format(pior),setup="from __main__ import bubble_sort",number=1))
