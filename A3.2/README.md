<center>SC3314 – Inteligencia Artificial Universidad de Monterrey Dr. Antonio Martínez Torteya</center>

# A3.2 Redes Neuronales

En esta actividad se trabajó con la base de datos de imágenes del MNIST. Se entrenó un modelo de Redes Neuronales con capas densas para poder clasificar dígitos del 0 al 9. Se compararon el *accuracy* para los subconjuntos de entrenamiento, validación y de prueba, y observar si hubo algún problema de sobreajuste. Después se generaron 50 imágenes (5 para cada dígito), con el fin de darle al modelo imágenes que nunca había visto, y con una esctructura o forma no tan "ordenada" como lo espera para avaluar su desempeño. Al comparar el desempeño del modelo, se generaron 3 nuevas mejoras para tener mejores resultados, y por último se implementó este modelo para que hiciera predicciones con imágenes en tiempo real a través de una Webcam. 

Puesto que la el modelo se entrenó con GPU mediante Google Colab, y la implementación se realizó con CPU mediante VS Code, la estructura de esta actividad la decidí organizar de la siguiente manera:

* Los puntos 1 y 2 con markdown en formato .ipynb y HTML
* El punto 3 será un link de Drive para las 50 imagenes generadas
* El punto 4 será un un archivo .py donde se implementa el modelo en VS Code, y se observa el desempeño en las 50 imágenes generadas
* El punto 5 será nuevamente un archivo con las mejoras que se le hicieron al modelo, explicadas en markdown. (formato .ipynb y HTML)
* El punto 6 será un archivo .py donde se implenete el modelo con las mejoras del punto 5, pero ahora haciando predicciones en tiempo real utilizando la Webcam del dispositivo. 
  
## Link al Pages 

[GitHub Pages](https://livingcheerios.github.io/Inteligencia-Artificial/A3.1/index.html)  

Aquí se encuentran los distintos archivos de esta actividad:
- [Reporte para los puntos 1. y 2. en formato ipynb](https://github.com/LivingCheerios/Inteligencia-Artificial/blob/main/A3.1/A31%20SVM%20y%20multiple%20testing%20%20.ipynb)
- [Reporte en formato html](https://github.com/LivingCheerios/Inteligencia-Artificial/blob/main/A3.1/A31%20SVM%20y%20multiple%20testing%20%20.html)
