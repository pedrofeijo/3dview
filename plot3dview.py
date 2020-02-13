import pptk
import numpy as np
arquivo= "/home/feijo/Documentos/feijo/carvao_ufc/pontos_1574700886/pontos_1574700886.txt" 
dados= np.loadtxt(arquivo, delimiter= ' ') #padronizar o formato txt com ou sem virgula dkdkke
dados= dados[:,:3] # ler até a 3 coluna
v = pptk.viewer(dados) # visualizar em tons de cinza
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)


