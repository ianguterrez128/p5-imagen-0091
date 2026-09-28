import cv2 
#leer la imagen con cv2 = computor vision
img = cv2.imread('pug.jpg')
#determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (554, 554, 3)
print(img.shape)
#mostrando imagen en ventas barra de titilo pug 0091'
cv2.imshow('pug 0091',img)
## tiempo de espera
cv2.waitkey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()