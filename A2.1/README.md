# A2.1 Regresión logística y validación cruzada

Desarrolla los siguientes puntos en una Jupyter Notebook, tratando, dentro de lo posible, que cada punto se trabaje en una celda distinta. Los comentarios en el código siempre son bienvenidos, de preferencia, aprovecha el markdown para generar cuadros de descripción que ayuden al lector a comprender el trabajo realizado.

1. Importa los datos a tu ambiente de trabajo. Especifica qué variable utilizarás como variable de salida, debe tratarse de una variable binaria. Si no hay ninguna variable binaria de interés, binariza la variable de salida que utilizaste en el proyecto (si trataste de predecir el precio de las casas, genera una variable que indique si una casa cuesta más que cierto monto, o menos).
   
2. Separa los datos en entrenamiento y prueba, con una relación de 80/20. Asegúrate de mantener un balance de clases (es decir, si en la base de datos hay 70% de observaciones de clase 0 y 30% de observaciones de clase 1, deberá mantenerse una proporción muy similar tanto en los datos de entrenamiento como en los de prueba), e imprime en consola las proporciones para los 3 grupos (datos originales, datos de entrenamiento, datos de prueba).

3. Usando los datos de entrenamiento, mide la exactitud de un modelo de regresión logística
usando alguna técnica de validación cruzada. Si tu base de datos era particularmente
compleja, puedes trabajar con 5 características de interés, en vez de con toda la base de
datos, o de tener que realizar un proceso de selección de características.

4. Entrena un modelo de regresión logística, similar al del punto anterior, pero utilizando todo el subconjunto de datos de entrenamiento. Usando dicho modelo, genera un vector de probabilidades para los datos de prueba. Genera una matriz de confusión y reporta la exactitud, sensibilidad y especificidad del modelo antes 3 diferentes umbrales (0.5, uno mayor, y uno menor).
   
5. Grafica la curva ROC para las probabilidades calculadas en el punto previo y reporta el valor de la AUC.

6. Interpreta los resultados del modelo, describiendo cómo es que cada variable afecta a la salida, en términos de los coeficientes generados.

Este proyecto incluye los siguientes documentos:
- [Reporte en formato ipynb]()
- [Reporte en HTML (GitHub Pages)]()  
- [Base de datos]()
