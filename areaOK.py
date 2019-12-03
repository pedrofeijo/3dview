
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


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


