# Developer: Pedro Feijó
############    Gerar slices e fechar poligonos ############
# https://plot.ly/python/alpha-shapes/

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
arquivo= "/home/feijo/Documents/carvao_ufc/pontos_1574700886/pontos_1574700886.txt" 
dados_df= np.loadtxt(arquivo, delimiter= ' ')

label= dados_df[:,-1] # todas as labels Y

# PLOTAR APENAS COM 1 ,
for lbl in range(0,int(label.max())):
    dados_label = dados_df[dados_df[:,-1]==lbl]
    print(dados_label.shape, lbl)

    dados_df2 = dados_label[:,:3] # ajustar arquivo txt - (linha , coluna)
    dados= dados_df2[dados_df2[:,0].argsort()] #ordenar eixo x
    dados_x= dados[:,0]
    dados_y= dados[:,1]
    dados_z= dados[:,2]

    points = [(y,z) for y,z in zip(dados_y,dados_z)]

    #DEFININDO ALPHA
    alpha_shape = alphashape.alphashape(points, 0.)
    # alpha_shape = alphashape.alphashape(points) # calculo do alpha automatico
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points))
    
    plt.xlim([np.min(dados_y), np.max(dados_y)])
    plt.ylim([np.min(dados_z), np.max(dados_z)])
    plt.axis("off") 

    ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
    # plt.show()
    plt.xlim([np.min(dados_y), np.max(dados_y)]) # limitando o espaço de plotar em y
    plt.ylim([np.min(dados_z), np.max(dados_z)]) # limitando o espaço de plotar em z
    plt.axis("off") # sem eixos

    fig.savefig('/home/feijo/Documents/carvao_ufc/imgslice/fig01_{}.png'.format(lbl))
    plt.close()

    # # PLOTAR APENAS COM 1 ,
    # for j in range(0,int(label.max())):
    #     contador = label.tolist().count(j)
    #     print(contador)
    #     for i in range(contador):
            
    #         points = [(y,z) for y,z in zip(dados_y[i*contador: (i+1)*contador],dados_z[i*contador: (i+1)*contador])]
        
    #         #DEFININDO ALPHA
    #         alpha_shape = alphashape.alphashape(points, 0.)
    #         # alpha_shape = alphashape.alphashape(points) # calculo do alpha automatico

    #         fig, ax = plt.subplots()
    #         ax.scatter(*zip(*points))
            
    #         plt.xlim([np.min(dados_y), np.max(dados_y)])
    #         plt.ylim([np.min(dados_z), np.max(dados_z)])
    #         plt.axis("off") 

    #         # fig.savefig('/home/feijo/Documents/carvao_ufc/pilhasegmentada2/fig01_{}.png'.format(i))

    #         ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
    #         # plt.show()
    #         plt.xlim([np.min(dados_y), np.max(dados_y)]) # limitando o espaço de plotar em y
    #         plt.ylim([np.min(dados_z), np.max(dados_z)]) # limitando o espaço de plotar em z
    #         plt.axis("off") # sem eixos 

    #         fig.savefig('/home/feijo/Documents/carvao_ufc/imgslice/fig01_{}.png'.format(i))

    #         plt.close()





    #     # for j in range(len(contador)):
    #     #     points = [(y,z) for y,z in zip(dados_y,dados_z)]
    #     #     #DEFININDO ALPHA
    #     #     alpha_shape = alphashape.alphashape(points, 0.)
    #     #     # alpha_shape = alphashape.alphashape(points) # calculo do alpha automatico
    #     #     fig, ax = plt.subplots()
    #     #     ax.scatter(*zip(*points))
            
    #     #     plt.xlim([np.min(dados_y), np.max(dados_y)])
    #     #     plt.ylim([np.min(dados_z), np.max(dados_z)])
    #     #     plt.axis("off") 
    #     #     # fig.savefig('/home/feijo/Documents/carvao_ufc/pilhasegmentada2/fig01_{}.png'.format(i))
    #     #     ax.add_patch(PolygonPatch(alpha_shape, alpha=0.2))
    #     #     # plt.show()
    #     #     plt.xlim([np.min(dados_y), np.max(dados_y)]) # limitando o espaço de plotar em y
    #     #     plt.ylim([np.min(dados_z), np.max(dados_z)]) # limitando o espaço de plotar em z
    #     #     plt.axis("off") # sem eixos

    #     #     fig.savefig('/home/feijo/Documents/carvao_ufc/imgslice/fig01_{}.png'.format(i))
    #     #     plt.close()
