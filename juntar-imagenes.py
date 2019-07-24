from PIL import Image
from imutils import paths
import os
import argparse

# como el script se ejecuta desde la consola, se crean dos argumentos
ap = argparse.ArgumentParser()

# --input es la ruta de la carpeta con los archivos
ap.add_argument("-l", "--left", required=True,
	help="ruta de la carpeta con los archivos")

# --input es la ruta de la carpeta con los archivos
ap.add_argument("-r", "--right", required=True,
	help="ruta de la carpeta con los archivos")

# --output es la ruta de la carpeta de destino
ap.add_argument("-o", "--output", required=True,
    help="ruta de la carpeta de destino")

# guarda los argumentos recibidos en una variable
args = vars(ap.parse_args())

# variable del total de imagenes
total = 0

# abre cada una de las imagenes en la carpeta del input
for imagePath in paths.list_images(args["left"]):
    try:
        total += 1
        path_right = "render" + str(total).zfill(4) + ".png"
        final_path = os.path.join(args["right"], path_right)
        im_right = Image.open(final_path)
        im_right.thumbnail((400,400))
        
        im_left = Image.open(imagePath)
        im_left.thumbnail((400,400))

        new_img = Image.new("RGB", (800, 266))
        new_img.paste(im_left, (0,0))
        new_img.paste(im_right, (400,0))

        new_img.save(os.path.join(args["output"], "render" + str(total).zfill(4) + ".jpg"))
    except:
        print("error")