# Developer: Pedro Feijó
############    Gerar slices ############
############    Gerar slices ############
############    Gerar slices ############
import pptk
import pandas as pd
import numpy as np #somente dados numéricos
import matplotlib.pyplot as plt
import sys
from descartes import PolygonPatch
import alphashape
import random
from PIL import Image

#LER NUVEM DE PONTOS
arquivo= "/home/feijo/Documents/carvao_ufc/pilhas_segmentadas/pilha1_chao.txt" 
dados_df= np.loadtxt(arquivo, delimiter= ',')
dados=dados_df[dados_df[:,0].argsort()] #ordenar eixo x
dados_x= dados[:,0]
dados_y= dados[:,1]
dados_z= dados[:,2]
# print(dados [0,1:3])
# print(dados_y,dados_z)
# v= pptk.viewer(dados,dados_x)
# plt.plot(dados_y,dados_z) #visualizar em 2d
# plt.show()

# SEPARAR EM SLICES NO EIXO X COM INTERVALOR DE 1000
intervalo= 1000 # se ficar menor não fecha o polígono
for i in range(len(dados_x)//intervalo):
    points = [(y,z) for y,z in zip(dados_y[i*intervalo: (i+1)*intervalo],dados_z[i*intervalo: (i+1)*intervalo])]

    #DEFININDO ALPHA
    alpha_shape = alphashape.alphashape(points, 0.)
    # alpha_shape = alphashape.alphashape(points) # calculo do alpha automatico

    fig, ax = plt.subplots()
    ax.scatter(*zip(*points))
    
    plt.xlim([np.min(dados_y), np.max(dados_y)])
    plt.ylim([np.min(dados_z), np.max(dados_z)])
    plt.axis("off") 

    # fig.savefig('/home/feijo/Documents/carvao_ufc/pilhasegmentada2/fig01_{}.png'.format(i))

    ax.add_patch(PolygonPatch(alpha_shape, alpha=5))
    # plt.show()
    plt.xlim([np.min(dados_y), np.max(dados_y)]) # limitando o espaço de plotar em y
    plt.ylim([np.min(dados_z), np.max(dados_z)]) # limitando o espaço de plotar em z
    plt.axis("off") # sem eixos 

    fig.savefig('/home/feijo/Documents/carvao_ufc/pilhasegmentada1/fig02_{}.png'.format(i))
    print(i) 
    plt.close()

total=0
for i in range(0,1333):
    img = np.asarray(Image.open("/home/feijo/Documents/carvao_ufc/pilhasegmentada1/fig02_{}.png".format(i)).convert('L'))


# img = np.asarray(Image.open("/home/feijo/Documents/carvao_ufc/caixa/fig02_60.png").convert('L'))
    img = 1 * (img < 255)
    m,n = img.shape
    total += img.sum() # guardar e somar as areas de todos slices

# use np.sum to count white pixels
# m*n valida que todas as imagens possuem dimensões iguais
    print("{} white pixels, out of {} pixels in total.".format(img.sum(), m*n))
    plt.imshow(img) # show as black and white
    plt.axis("off")
    
    
print("Número total de pixels {}".format(total))

    # plt.show()


somaslices = total*1000
volumeareaporpixels= somaslices*1.0686654023316165e-06 #relação pixels to m3
print(volumeareaporpixels)



    








