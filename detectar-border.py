from PIL import Image
from imutils import paths
import os
import argparse
import cv2

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
        img = cv2.imread(imagePath,0)

        # extraer border
        edges = cv2.Canny(img,256,256)
        # invertir color imaagen
        newBordes = cv2.bitwise_not(edges)
        # output
        cv2.imwrite(os.path.join(args["output"], "render" + str(total).zfill(4) + ".jpg"),newBordes)

        total += 1
    except:
        print("error")