# importar las librerias necesarias
from imutils import paths
import argparse
import requests
import cv2
import os

# como el script se ejecuta desde la consola, se crean dos argumentos
ap = argparse.ArgumentParser()

# --urls es la ruta del archivo urls.txt que se creo desde la consola del navegador
ap.add_argument("-u", "--urls", required=True,
	help="ruta al archivo que contiene las URLs")

# --output es la ruta de la carpeta en donde se van a descargar las imagenes
ap.add_argument("-o", "--output", required=True,
	help="ruta de la carpeta para descargar las imagenes")

# guarda los argumentos recibidos en una variable
args = vars(ap.parse_args())

# crea una variable con todas las URLs para iterar mas adelante
rows = open(args["urls"]).read().strip().split("\n")

# variable que almacena el numero de imagenes descargadas
total = 0

# loop las URLs
for url in rows:
	try:
		# intenta descargar la imagen
		r = requests.get(url, timeout=60)
 
		# guarda la imagen en el disco
		p = os.path.sep.join([args["output"], "{}.jpg".format(
			str(total).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
 
		# actualiza el contador
		print("[INFO] descargado: {}".format(p))
		total += 1
 
	# errores
	except:
		print("[INFO] error descargando {}...saltando".format(p))

# abre cada una de las imagenes que acabamos de descargar
for imagePath in paths.list_images(args["output"]):
	# variable boolean que determina si la imagen se borra o no
	delete = False
 
	# intenta cargar la imagen
	try:
		image = cv2.imread(imagePath)
 
		# si la imagen es `None` entonces no puede leerse y debe borrarse
		if image is None:
			delete = True
 
	# si OpenCV bota error entonces la imagen esta danada y debe borrarse
	except:
		print("Except")
		delete = True
 
	# si la variable `delete` es True entonces borrar la imagen
	if delete:
		print("[INFO] borrando {}".format(imagePath))
		os.remove(imagePath)