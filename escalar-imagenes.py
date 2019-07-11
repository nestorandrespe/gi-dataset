from PIL import Image
from imutils import paths
import os
import argparse

# como el script se ejecuta desde la consola, se crean dos argumentos
ap = argparse.ArgumentParser()

# --input es la ruta de la carpeta con los archivos
ap.add_argument("-i", "--input", required=True,
	help="ruta de la carpeta con los archivos")

# --output es la ruta de la carpeta de destino
ap.add_argument("-o", "--output", required=True,
    help="ruta de la carpeta de destino")

# guarda los argumentos recibidos en una variable
args = vars(ap.parse_args())

# variable del total de imagenes
total = 0


# abre cada una de las imagenes en la carpeta del input
for imagePath in paths.list_images(args["input"]):
    try:
        # carga la imagen en una variable
        im = Image.open(imagePath)
        
        # guardar los tamanos de la imagen en unas variables
        w = im.size[0]
        h = im.size[1]

        # si la imagen es vertical
        if w < h:
            # calcula el sobrante y lo divide por dos para cortar la imagen en el centro
            restante = h - w
            restante = restante / 2
            cropped = im.crop((0, restante, w, w + restante))

        # si la imagen es horizontal
        elif w > h:
            # calcula el sobrante y lo divide por dos para cortar la imagen en el centro
            restante = w - h
            restante = restante / 2
            cropped = im.crop((restante, 0, restante + h, h))

        # si la imagen es mas grande que 400 x 400 la guarda
        if cropped.size[0] > 400:
            p = os.path.sep.join([args["output"], "{}.jpg".format(str(total).zfill(8))])
            cropped.thumbnail((400,400))
            cropped.save(p, 'JPEG')
            total += 1
            print("[INFO] imagen guardada")
        else:
            print("[INFO] imagen demasiado pequena")
    except:
        print("[INFO] error al cargar la imagen")