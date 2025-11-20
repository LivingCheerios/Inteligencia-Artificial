<center>SC3314 – Inteligencia Artificial Universidad de Monterrey Dr. Antonio Martínez Torteya</center>

# P P3 Redes Neuronales

Este es el repositorio para el proyecto del tercer parcial del curso de Inteligencia Artificial. En este proyecto, se importó la base de datos conteniendo imágenes con dígitos del 0-9. Se prepreprocesaron dichas imágenes, y se utilizaron para entrenar un modelo base de redes convolucionales, usando parte de los datos de entrenamiento como validación, y observando su desempeño en ambos subconjuntos. Luego se procedió a realizar mejorar a dicho modelo base, tanto en la arquitectura como en la forma de entrenamiento, teniendo al final 6 modelos diferentes. Se eligió el mejor usando la de mejor métrica de *accuracy*, y para dicho modelo se realizó una gráfica de su desempeño por cada época. Luego se procedió a entrenar un modelo con la misma arquitectura que el modelo ganador, pero puramente con datos de entrenamiento, sin separar en train-validation. Y se analizó su desempeño en la clasificacion de los digitos de la seccion *Test*.

Por último se hizo la implementación de predicción en tiempo real con Webcam. Como opción de puntos extras, se implementó también a un OCR. 

Puesto que la el modelo se entrenó con GPU mediante Google Colab, y la implementación se realizó con CPU mediante VS Code, la estructura de esta actividad la decidí organizar de la siguiente manera:

* Los puntos 1 y 2 con markdown en formato .ipynb y HTML
* Los puntos 3 y 4 estarán en otro notebook con markdown en formato .ipynb y HTML
* El punto 5 estará en otro notebook con markdown en formato .ipynb y HTML
* El punto 6 será un archivo .py donde se implenete el modelo con las mejoras del punto 5, pero ahora haciando predicciones en tiempo real utilizando la Webcam del dispositivo, así como el video mostrando su funcionalidad.
* Para la implementación del OCR, también se incluirá el .py y el video correspondiente

* Nota: Los links de los reportes en formato HTML estando en el GitHub Pages, funcionan como una subpagina del pages, donde se desplgará el reporte. Estando en el repositorio, si se hace click al link del reporte en formato HTML, llevará al archivo con el código HTML.

## Link al Pages 

[GitHub Pages](https://livingcheerios.github.io/Inteligencia-Artificial/P_P3) 
  

Aquí se encuentran los distintos archivos de esta actividad:

**Modelo inicial**
__________________________________________________________________________________________________________________________________________
- [Reporte para los puntos 1. y 2. en formato HTML](Modelo1.html)
- [Reporte para los puntos 1. y 2. en formato ipynb](https://github.com/LivingCheerios/Inteligencia-Artificial/blob/main/P_P3/Modelo1.ipynb)

  
  **Base de imágenes utilizada**
__________________________________________________________________________________________________________________________________________
- [Link a la carpeta con la base de datos](https://drive.google.com/drive/folders/1RKfdeZpSp69w5gLsqeqYNoIpCxmUJjHl?usp=sharing)

  **Modelos con Modificaciones y evaluación del mejor modelo**
__________________________________________________________________________________________________________________________________________
- [Reporte para el punto 3 y 4 en en formato HTML](Models2_6.html)
- [Reporte para el punto 3 y 4 en en formato ipynb](https://github.com/LivingCheerios/Inteligencia-Artificial/blob/main/P_P3/Models2_6.ipynb)


 **Evaluación del modelo entrenado con todas las imágenes**
__________________________________________________________________________________________________________________________________________
- [Reporte para el punto 5 en formato HTML](A32_3.html)
- [Reporte para el punto 5 en formato ipynb](https://github.com/LivingCheerios/Inteligencia-Artificial/blob/main/A3.2/A32_3.ipynb)

**Archivo para clasificaciónes en tiempo real**
_____________________________________________________________________________________________
- [Reporte para el punto 5 en formato HTML](A32_3.html)

**Archivo para clasificaciónes en tiempo real con OCR**
_____________________________________________________________________________________________
- [Reporte para el punto 5 en formato HTML](A32_3.html)
