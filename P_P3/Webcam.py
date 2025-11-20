import cv2 as cv
import numpy as np
import tensorflow as tf

# Cargar el modelo
model = tf.keras.models.load_model("best_model.keras")

# Inicializar la cámara
cap = cv.VideoCapture(0)
img_height, img_width = 28, 28  # Dimensiones de entrada esperadas por el modelo

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
    
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

       
        blurred = cv.GaussianBlur(gray, (3, 3), 0)  # Difuminar para reducir ruido
        _, thresh = cv.threshold(blurred, 80, 255, cv.THRESH_BINARY_INV)  # Umbral

        # Redimensionar la imagen a 28x28 para que el modelo pueda hacer la predicción
        resized = cv.resize(thresh, (img_height, img_width))

        # Normalizar la imagen a rango [0,1]
        normalized = resized.astype("float32") / 255.0
        input_img = normalized.reshape(1, 28, 28, 1)

        # Predicción
        prediction = model.predict(input_img)
        predicted_label = np.argmax(prediction)  # Etiqueta predicha
        predicted_prob = np.max(prediction)  # Probabilidad de la predicción

        # Mostrar la probabilidad para cada número en rojo, y la "ganadora" en verde
        for i, prob in enumerate(prediction[0]):
            color = (0, 0, 255) if i != predicted_label else (0, 255, 0)  # Rojo por defecto, Verde para la mejor
            cv.putText(frame, f'{i}: {prob:.2f}', (10, 30 + i * 30),  
                       cv.FONT_HERSHEY_SIMPLEX, 0.7, color, 2, cv.LINE_AA)


        # Mostrar la imagen filtrada/umbralizada
        cv.imshow('Imagen Filtrada', thresh)

        # Mostrar la imagen procesada
        cv.imshow('Predicción en tiempo real', frame)

        # Tecla para terminar el programa
        if cv.waitKey(1) & 0xFF == ord('d'):
            break

except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv.destroyAllWindows()

