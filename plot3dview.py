import pptk
import numpy as np
arquivo= "/home/feijo/Documents/carvao_ufc/pontos_ida.txt" 
dados= np.loadtxt(arquivo, delimiter= ' ') #padronizar o formato txt com ou sem virgula

v = pptk.viewer(dados) # visualizar em tons de cinza
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)

dados_z= dados[:,2]
aux= np.mean(dados_z)
v = pptk.viewer(dados, aux[:,2]) # visualização colorida referencia em Z
