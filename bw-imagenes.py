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

        # convierte la imagen a escala de grises
        bw = im.convert("L")
        p = os.path.sep.join([args["output"], "{}.jpg".format(str(total).zfill(8))])
        bw.save(p, 'JPEG')
        total += 1
        print("[INFO] imagen guardada")
    except:
        print("[INFO] error al cargar la imagen")