# gi-dataset
Scripts para extraer imágenes de Google para armar un dataset.
Basado en las instrucciones publicadas en [pyimagesearch](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/).

## Pasos a seguir
Realizar una búsqueda en Google Images y abrir la consola javascript del navegador.

```javascript
// crea un nuevo elemento <script>
var script = document.createElement('script');

// añadir jquery al nuevo elemento
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";

// añadir el script al <head> del documento
document.getElementsByTagName('head')[0].appendChild(script);

// usando jquery se seleccionan los elementos que contienen las urls de las imagenes y se añaden a un arreglo
var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });

// se convierten los enlaces en el arreglo a un string con saltos de linea entre cada elemento
var textToSave = urls.toArray().join('\n');

// se crea un nuevo elemento <a> para descargar el archivo de texto
var elementoDescarga = document.createElement('a');

// se cambia el link del nuevo elemento [href] para que descargue un documento de texto
elementoDescarga.href = 'data:attachment/text,' + encodeURI(textToSave);

// se cambia el destino del elemento a para que cargue en una nueva ventana
elementoDescarga.target = '_blank';

// se pone un nombre al archivo
elementoDescarga.download = 'urls.txt';

// click y descarga del nuevo documento
elementoDescarga.click();
```

Una vez se haya descargado el archivo urls.txt, correr en la consola el archivo python especificando --urls [la ruta al archivo] y --output [la carpeta de destino]

```bash
python descarga-imagenes.py --urls [ruta al archivo] --output [ruta de destino]
```

Cuando ya esten descargadas las imagenes se puede usar el archivo escalar-imagenes.py para escalar las imagenes a un cuadrado de 400 x 400 y ser usadas para un dataset especificando --input [la carpeta donde se descargaron las imágenes] y el --output [la carpeta donde se van a guardar las nuevas versiones]

```bash
python escalar-imagenes.py --input [ruta de la carpeta input] --output [ruta de destino]
```