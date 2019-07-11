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
```

