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
import os   
import glob 


#LER NUVEM DE PONTOS 
# arquivo= "/home/feijo/Documents/carvao_ufc/CHAO/pilhacompleta.asc" 

arquivo= "/home/feijo/Documents/carvao_ufc/pilha.txt" 
dados_df= np.loadtxt(arquivo, delimiter= ' ')
# dados= dados_df[:,:3] # ajustar arquivo txt - (linha , coluna)
dados=dados_df[dados_df[:,0].argsort()] #ordenar eixo x
dados_x= dados[:,0]
dados_y= dados[:,1]
dados_z= dados[:,2]

a = np.mean(dados_z)
b= np.min(dados_z)
c= np.max(dados_z)
print(dados_z)
print("Média {} Mínimo {} Máximo {}".format(a,b,c))

v = pptk.viewer(dados_df) # visualizar em tons de cinza

limiarz= (b*1.12)
# newz = dados_z - novodados_z
# print(limiarz)
# print(newz)

# novoa = np.mean(novodados_z)
# novob= np.min(novodados_z)
# novoc= np.max(novodados_z)
# print("Média {} Mínimo {} Máximo {}".format(novoa,novob,novoc))

# new_dados_x= dados_x
# new_dados_y= dados_y
# new_dados_z= newz

new_dados_df = np.vstack((dados_x,dados_y,dados_z))
new_dados_df = new_dados_df.T
new_dados_df =  new_dados_df[new_dados_df[:,-1]>limiarz] 
np.savetxt("hercules12.txt", new_dados_df) #transposta dos dados

v = pptk.viewer(new_dados_df) # visualizar em tons de cinza
